import torch
import numpy as np
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from transformers import AutoTokenizer


categories = set()


class PeopleDaily(Dataset):
    def __init__(self, data_file):
        self.data = self.load_data(data_file)

    def load_data(self, data_file):
        Data = {}
        with open(data_file, "rt", encoding="utf-8") as f:
            for idx, line in enumerate(f.read().split("\n\n")):
                if not line:
                    break
                sentence, labels = "", []
                for i, item in enumerate(line.split("\n")):
                    char, tag = item.split(" ")
                    sentence += char
                    if tag.startswith("B"):
                        labels.append([i, i, char, tag[2:]])  # Remove the B- or I-
                        categories.add(tag[2:])
                    elif tag.startswith("I"):
                        labels[-1][1] = i
                        labels[-1][2] += char
                Data[idx] = {"sentence": sentence, "labels": labels}
        return Data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


train_data = PeopleDaily("/home/nio/personal/magic_repo/oneone/run_transformer/china-people-daily-ner-corpus/example.train")
valid_data = PeopleDaily("/home/nio/personal/magic_repo/oneone/run_transformer/china-people-daily-ner-corpus/example.dev")
test_data = PeopleDaily("/home/nio/personal/magic_repo/oneone/run_transformer/china-people-daily-ner-corpus/example.test")


id2label = {0: "O"}
for c in list(sorted(categories)):
    id2label[len(id2label)] = f"B-{c}"
    id2label[len(id2label)] = f"I-{c}"
label2id = {v: k for k, v in id2label.items()}


checkpoint = "bert-base-chinese"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)


def collote_fn(batch_samples):
    batch_sentence, batch_tags = [], []
    for sample in batch_samples:
        batch_sentence.append(sample["sentence"])
        batch_tags.append(sample["labels"])
    batch_inputs = tokenizer(batch_sentence, padding=True, truncation=True, return_tensors="pt")
    batch_labels = np.zeros(batch_inputs["input_ids"].shape, dtype=int)
    for s_idx, sentence in enumerate(batch_sentence):
        encoding = tokenizer(sentence, truncation=True)
        batch_labels[s_idx][0] = -100  # 将 [CLS] token 的 loss 掩码设为 -100
        batch_labels[s_idx][len(encoding.tokens()) - 1 :] = -100  # 将 [SEP] 和 [PAD] token 的 loss 掩码设为 -100
        for char_start, char_end, _, tag in batch_tags[s_idx]:
            token_start = encoding.char_to_token(char_start)  # 将原文位置映射到切分后的 token 位置
            token_end = encoding.char_to_token(char_end)  # 将原文位置映射到切分后的 token 位置
            batch_labels[s_idx][token_start] = label2id[f"B-{tag}"]
            batch_labels[s_idx][token_start + 1 : token_end + 1] = label2id[f"I-{tag}"]
    return batch_inputs, torch.tensor(batch_labels)


train_loader = DataLoader(train_data, batch_size=4, shuffle=True, collate_fn=collote_fn)
valid_loader = DataLoader(valid_data, batch_size=4, collate_fn=collote_fn)
test_dataloader = DataLoader(test_data, batch_size=4, shuffle=False, collate_fn=collote_fn)

batch_X, batch_y = next(iter(train_loader))
print("batch_X shape:", {k: v.shape for k, v in batch_X.items()})
print("batch_y shape:", batch_y.shape)
print(batch_X)
print(batch_y)
