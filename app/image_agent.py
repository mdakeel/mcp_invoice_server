import base64
import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def parse_invoice_image(image_path):
    base64_image = encode_image(image_path)

    prompt = """
    You are an invoice parsing assistant. Extract the following fields from the invoice image:
    
    - Client Name
    - Invoice Number
    - Total Amount
    
    Respond ONLY in JSON format like:
    {
      "client_name": "Rahul Sharma",
      "invoice_number": "INV-2023-001",
      "total_amount": "₹1250.00"
    }
    Do not include any explanation or extra text.
    """


    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=800
    )

    raw = response.choices[0].message.content
    # print("\n🧠 GPT Raw Response:\n", raw)
    cleaned = raw.strip().strip("`").replace("json", "").strip()

    try:
        parsed = json.loads(cleaned) 
    except json.JSONDecodeError:
        parsed = {"client_name": "", "invoice_number": "", "total_amount": "", "raw": raw}
        
    return parsed
