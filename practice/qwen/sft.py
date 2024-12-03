import os
import torch
from datasets import load_dataset, DatasetDict
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from transformers import DataCollatorForSeq2Seq
from peft import get_peft_model, LoraConfig, TaskType
from torch.nn.utils.rnn import pad_sequence


dataset = load_dataset("allenai/tulu-3-sft-mixture")


# def subsample_dataset(dataset, percentage=0.05):
#     # 确保 percentage 在 0 到 1 之间
#     assert 0 < percentage <= 1, "Percentage must be between 0 and 1."

#     subsampled_dict = {}
#     for split in dataset.keys():  # 针对 train 和 validation 分别处理
#         split_dataset = dataset[split]
#         total_samples = len(split_dataset)
#         num_samples = max(1, int(total_samples * percentage))  # 至少保留一个样本
#         subsampled_dict[split] = split_dataset.select(range(num_samples))  # 选择前 num_samples 个样本
#     return DatasetDict(subsampled_dict)


# # 1% 的数据作为快速测试
# dataset = subsample_dataset(dataset, percentage=0.01)

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B")


train_test_split = dataset["train"].train_test_split(test_size=0.1)
dataset = DatasetDict(
    {
        "train": train_test_split["train"],
        "validation": train_test_split["test"],
    }
)


def process_func(examples):
    # model_inputs_text = []
    # model_outputs_text = []
    MAX_LENGTH = 1024

    total_input_ids, total_attention_mask, total_labels = [], [], []

    for message in examples["messages"]:
        user_input = [msg["content"] for msg in message if msg["role"] == "user"]
        assistant_output = [msg["content"] for msg in message if msg["role"] == "assistant"]
        instruction_text = ""
        for i in range(len(user_input)):
            instruction_text += f"<|im_start|>user\n{user_input[i]}<|im_end|>\n<|im_start|>assistant\n"
            response_text = assistant_output[i]

            instruction = tokenizer(instruction_text, add_special_tokens=False, truncation=True, max_length=MAX_LENGTH)
            response = tokenizer(response_text, add_special_tokens=False, truncation=True, max_length=MAX_LENGTH)

            input_ids = instruction["input_ids"] + response["input_ids"] + [tokenizer.pad_token_id]
            attention_mask = instruction["attention_mask"] + response["attention_mask"] + [1]  # 因为 eos token 咱们也是要关注的所以 补充为1
            labels = [-100] * len(instruction["input_ids"]) + response["input_ids"] + [tokenizer.pad_token_id]

            if len(input_ids) > MAX_LENGTH:
                input_ids = input_ids[:MAX_LENGTH]
                attention_mask = attention_mask[:MAX_LENGTH]
                labels = labels[:MAX_LENGTH]

            total_input_ids.append(input_ids)
            total_attention_mask.append(attention_mask)
            total_labels.append(labels)

            # model_inputs_text.append(instruction_text)
            # model_outputs_text.append(response_text)
            instruction_text += response_text + "<|im_end|>\n"

    # for i in range(len(model_inputs_text)):
    #     print(f"model_inputs[{i}]:\n {model_inputs_text[i]}")
    #     print(f"model_outputs[{i}]:\n {model_outputs_text[i]}")

    padded_input_ids = pad_sequence([torch.tensor(x) for x in total_input_ids], batch_first=True, padding_value=tokenizer.pad_token_id)
    padded_attention_mask = pad_sequence([torch.tensor(x) for x in total_attention_mask], batch_first=True, padding_value=0)
    padded_labels = pad_sequence([torch.tensor(x) for x in total_labels], batch_first=True, padding_value=-100)

    return {
        "input_ids": padded_input_ids,
        "attention_mask": padded_attention_mask,
        "labels": padded_labels,
    }


tokenized_dataset = dataset.map(process_func, batched=True, remove_columns=["id", "messages", "source"])

config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    inference_mode=False,
    r=8,
    lora_alpha=32,
    lora_dropout=0.1,
)


model = get_peft_model(model, config)


training_args = TrainingArguments(
    output_dir="./qwen2.5-1.5b-finetuned",  # 模型输出路径
    per_device_train_batch_size=4,  #
    gradient_accumulation_steps=8,  #
    num_train_epochs=2,  # 总共训练的 epoch 数
    save_steps=500,  # 每训练多少个 step 保存一次
    save_total_limit=2,  # 总共保存的模型数
    learning_rate=5e-5,
    warmup_steps=100,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=100,
    fp16=True,  # 如果 GPU 支持混合精度
)

# 数据对齐处理器
data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

trainer.train()
