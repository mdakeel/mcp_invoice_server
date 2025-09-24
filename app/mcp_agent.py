import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_with_chatgpt(text):
    prompt = f"""Extract the following from this invoice text:
    - client name
    - Invoice numbers
    - All amounts
    - Total amount

    Text:
    {text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
