import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

messages = [
    {
        "role": "system",
        "content": "You are my mentor and business consultant. You will provide me with guidance and advice on how to start my own brand and business. Please provide me with actionable steps and strategies to help me achieve my goals.",
    },
    {
        "role": "user",
        "content": "I want consultation on how I can start my brand. I want to start my own something, and I am stuck at an end position. How can I solve my problem? Please tell me. ",
    },
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    temperature=2,
)

print(response.choices[0].message.content)