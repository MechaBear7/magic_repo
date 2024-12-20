import os

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["HF_HOME"] = "/home/helei.yang/codes/hf_home"
import json
import torch
import torch.nn.functional as F
import random
import numpy as np
from tqdm.auto import tqdm
from torch.utils.data import Dataset, DataLoader
from transformers import get_scheduler
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from torch.optim import AdamW
from sacrebleu.metrics import BLEU

from torch.utils.tensorboard import SummaryWriter


def seed_everything(seed=1029):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True


class MyDataset(Dataset):
    def __init__(self, data_file):
        self.data = self.load_data(data_file)

    def load_data(self, data_file):
        Data = []
        with open(data_file, "rt", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                sample = json.loads(line.strip())
                Data.append(sample)
        return Data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


def train_loop(
    dataloader, model, optimizer, lr_scheduler, epoch, steps, total_loss, tf_writer
):
    progress_bar = tqdm(range(len(dataloader)))
    progress_bar.set_description(f"loss: {0:>7f}")
    finish_batch_num = (epoch - 1) * len(dataloader)

    model.train()
    for idx, batch in enumerate(dataloader):
        batch = batch.to(device)
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()

        tf_writer.add_scalar("loss", loss, steps)

        optimizer.step()
        lr_scheduler.step()
        optimizer.zero_grad()

        total_loss += loss.item()
        progress_bar.set_description(
            f"loss: {total_loss / (idx + finish_batch_num + 1):>7f}"
        )
        progress_bar.update(1)

        steps += 1

    return total_loss, steps


def test_loop(dataloader, model, steps, tokenizer, bleu, tf_writer):
    preds, labels = [], []

    model.eval()
    print_debug = False
    for batch in tqdm(dataloader):
        batch = batch.to(device)
        with torch.no_grad():
            generated_tokens = model.generate(
                batch["input_ids"],
                attention_mask=batch["attention_mask"],
                max_length=512,
            )
        generated_texts = tokenizer.batch_decode(
            generated_tokens, skip_special_tokens=True
        )

        if not print_debug:
            input_tokens = batch["input_ids"]
            input_texts = tokenizer.batch_decode(input_tokens, skip_special_tokens=True)

        label_tokens = batch["labels"]
        label_tokens = torch.where(
            label_tokens != -100, label_tokens, tokenizer.pad_token_id
        )
        target_texts = tokenizer.batch_decode(label_tokens, skip_special_tokens=True)

        preds += [pred.strip() for pred in generated_texts]
        labels += [[label.strip()] for label in target_texts]
        if not print_debug:
            model_inputs = [input.strip() for input in input_texts]
            preds_ = [pred.strip() for pred in generated_texts]
            labels_ = [[label.strip()] for label in target_texts]
            for idx in range(len(input_texts)):
                print("model_input: ", model_inputs[idx])
                print("model_output: ", preds_[idx])
                print("model_labels: ", labels_[idx])
            print_debug = True

    score = bleu.corpus_score(preds, labels).score
    tf_writer.add_scalar("bleu", score, steps)
    return score


def train():
    epoch_num = 30
    learning_rate = 1e-4

    train_dataset = "/home/helei.yang/codes/llms/dataset/hw1/train.json"
    val_dataset = "/home/helei.yang/codes/llms/dataset/hw1/dev.json"
    output_path = "/home/helei.yang/codes/llms/output/hw1"

    train_data = MyDataset(train_dataset)
    val_data = MyDataset(val_dataset)

    model_name = "uer/t5-base-chinese-cluecorpussmall"

    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model = model.to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    def collate_function(batch):
        batch_inputs = [
            f'问题：{sample["question"]}{tokenizer.sep_token}原文：{sample["context"]}'
            for sample in batch
        ]
        batch_targets = [
            f'答案：{sample["answer"]}{tokenizer.eos_token}' for sample in batch
        ]

        batch_data = tokenizer(
            batch_inputs,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors="pt",
        )

        batch_labels = tokenizer(
            batch_targets,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors="pt",
        )["input_ids"]

        decoder_input_ids = batch_labels[:, :-2]
        decoder_input_ids = F.pad(
            decoder_input_ids, (0, 2), value=tokenizer.pad_token_id
        )

        labels = batch_labels[:, 1:-1]
        labels = F.pad(labels, (0, 2), value=-100)

        # 将 labels 添加到 batch_data
        batch_data["labels"] = labels
        batch_data["decoder_input_ids"] = decoder_input_ids

        # 移除不需要的 token_type_ids
        if "token_type_ids" in batch_data:
            del batch_data["token_type_ids"]

        return batch_data

    train_dataloader = DataLoader(
        train_data, batch_size=32, shuffle=True, collate_fn=collate_function
    )
    val_dataloader = DataLoader(
        val_data, batch_size=32, shuffle=False, collate_fn=collate_function
    )

    optimizer = AdamW(model.parameters(), lr=learning_rate)
    lr_scheduler = get_scheduler(
        "linear",
        optimizer=optimizer,
        num_warmup_steps=0,
        num_training_steps=epoch_num * len(train_dataloader),
    )
    tf_output_path = os.path.join(output_path, "tensorboard")
    os.makedirs(tf_output_path, exist_ok=True)
    tf_writer = SummaryWriter(tf_output_path)

    bleu = BLEU()

    steps = 0
    total_loss = 0.0
    for t in range(epoch_num):
        print(f" ------- Epoch {t+1}/{epoch_num}  ------- ")
        total_loss, steps = train_loop(
            train_dataloader,
            model,
            optimizer,
            lr_scheduler,
            t + 1,
            steps,
            total_loss,
            tf_writer,
        )
        valid_bleu = test_loop(val_dataloader, model, steps, tokenizer, bleu, tf_writer)
        print(f"BLEU: {valid_bleu:>0.2f}\n")
        print("saving new weights...\n")
        torch.save(
            model.state_dict(),
            f"epoch_{t+1}_valid_bleu_{valid_bleu:0.2f}_model_weights.bin",
        )
    print("Done!")


def infer():
    model_name = "uer/t5-base-chinese-cluecorpussmall"

    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model = model.to(device)
    # 加载模型参数
    model.load_state_dict(torch.load("epoch_30_valid_bleu_0.00_model_weights
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    question = ""
    context = ""

    model_input = f"问题：{question}原文：{context}"
    tokenized_input = tokenizer(
        model_input, padding=True, truncation=True, max_length=512, return_tensors="pt"
    )
    with torch.no_grad():
        generated_tokens = model.generate(
            tokenized_input["input_ids"],
            attention_mask=tokenized_input["attention_mask"],
            max_length=512,
        )
    generated_texts = tokenizer.decode(generated_tokens)

    print(generated_texts)


if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using {device} device")
    seed_everything(2024)

    # train()
    infer()
