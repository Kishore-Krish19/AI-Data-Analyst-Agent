from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os
load_dotenv()
API_KEY = os.getenv("qwenAPI_TOKEN")

client = InferenceClient(
    api_key=API_KEY
)

print("🤖 Hugging Face Chatbot (type 'exit' to quit)\n")

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit" or user_input.lower() == "quit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="Qwen/Qwen3.6-35B-A3B",
        messages=messages,
        max_tokens=200
    )

    ai_reply = response.choices[0].message.content

    print("AI:", ai_reply, "\n")

    messages.append({
        "role": "assistant",
        "content": ai_reply
    })