import os
from transformers import pipeline

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# 情感分析
# classifier = pipeline("sentiment-analysis")
# result = classifier("I've been waiting for a HuggingFace course my whole life.")
# print(result)
# results = classifier(
#     [
#         "I've been waiting for a HuggingFace course my whole life.",
#         "I hate this so much!",
#     ]
# )
# print(results)


# 零样本分类
# classifier = pipeline("zero-shot-classification")
# result = classifier(
#     "This is a course about the Transformers library",
#     candidate_labels=["education", "politics", "business"],
# )
# print(result)


# 文本生成
# generator = pipeline("text-generation")
# results = generator("In this course, we will teach you how to")
# print(results)
# results = generator(
#     "In this course, we will teach you how to",
#     num_return_sequences=2,
#     max_length=50,
# )
# print(results)

# generator = pipeline("text-generation", model="distilgpt2")  # 指定使用的模型
# results = generator(
#     "In this course, we will teach you how to",
#     max_length=30,
#     num_return_sequences=2,
# )
# print(results)

# generator = pipeline("text-generation", model="uer/gpt2-chinese-poem")  # 指定使用的模型
# results = generator(
#     "[CLS] 万 叠 春 山 积 雨 晴 ，",
#     max_length=40,
#     num_return_sequences=2,
# )
# print(results)


# 遮盖词填充
unmasker = pipeline("fill-mask")
results = unmasker("This course will teach you all about <mask> models.", top_k=2)
print(results)


# 实体命名识别
ner = pipeline("ner", grouped_entities=True)
results = ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
print(results)
