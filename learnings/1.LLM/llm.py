import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

Client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
content = "Write a code for fibonacci series in python"
message = [{"role": role, "content": content}]
response = Client.chat.completions.create(
    model=model,
    messages=message,
)
print(response.choices[0].message.content)