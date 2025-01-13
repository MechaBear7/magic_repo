from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModel

if __name__ == "__main__":
    model_name = "Qwen/Qwen1.5-1.8B"

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_name, trust_remote_code=True).half().cuda()  # half precision
    model.eval()

    app = FastAPI()