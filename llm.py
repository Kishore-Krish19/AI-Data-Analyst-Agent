from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("qwenAPI_TOKEN")

client = InferenceClient(api_key=API_KEY)

def ask_llm(messages_or_prompt):
    # This allows the function to handle both single prompts and full chat histories
    if isinstance(messages_or_prompt, str):
        messages = [{"role": "user", "content": messages_or_prompt}]
    else:
        messages = messages_or_prompt

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-Coder-32B-Instruct", # Valid, powerful model for Data Analysis
        messages=messages,
        max_tokens=500
    )

    return response.choices[0].message.content