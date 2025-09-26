import os
import json
import re
from PyPDF2 import PdfReader
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4"
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def extract_invoice_fields(file_path: str, file_name: str):
    reader = PdfReader(file_path)
    text = "".join(page.extract_text() or "" for page in reader.pages)

    prompt = (
        "Extract the following fields from this invoice:\n"
        "1. client_name (string)\n"
        "2. invoice_amount (float)\n"
        "3. product_name (string or list of strings)\n"
        "Return result as a JSON object with keys exactly as specified.\n\n"
        f"Invoice text:\n{text}"
    )

    response = openai_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    print("\nGPT raw response:\n", response.choices[0].message.content)
    return parse_json(response.choices[0].message.content)

def parse_json(content):
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
    return {"error": "Failed to parse JSON", "raw": content}
