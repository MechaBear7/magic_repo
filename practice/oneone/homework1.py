import os
from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

model_name = "uer/t5-base-chinese-cluecorpussmall"


train_dataset = "/home/nio/personal/magic_repo/practice/oneone/dataset/train.json"

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


dataset = load_dataset("json", data_files=train_dataset)


def process_function(examples):
    questions = examples["question"]
    contexts = examples["context"]
    inputs = [f"question: {question} context: {context}" for question, context in zip(questions, contexts)]
    targets = examples["answer"]
    model_inputs = tokenizer(inputs, max_length=512, truncation=True)
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, max_length=512, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs


tokenized_datasets = dataset.map(process_function, batched=True)
