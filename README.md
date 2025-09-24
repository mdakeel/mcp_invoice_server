
# 🧠 MCP Invoice Server

A modular invoice parsing system powered by GPT-4o Vision — built for real-world invoices in both image and PDF formats. No Swagger, no uvicorn — just clean CLI testing and direct GPT integration.

## 🚀 What It Does

- 📸 Parses invoice images (JPG/PNG) using GPT-4o Vision
- 📄 Converts PDF invoices to images and parses them visually
- 🧪 Supports batch testing via CLI scripts
- 🔐 Uses `.env` for secure API key handling
- 🧼 Clean structure with modular agents and minimal boilerplate

## 📁 Project Structure

mcp_invoice_server/
├── app/
│   ├── main.py                    # FastAPI endpoints for image & PDF parsing
│   ├── parser.py                # PDF text extractor (legacy support)
│   ├── mcp_agent.py     # GPT agent for text-based invoices
│   ├── image_agent.py   # GPT Vision agent for image invoices
│   └── utils.py                  # (empty for now — reserved for future tools)
├── invoices/            # Sample invoice files
├── requirements.txt          # Dependencies
├── .env                 # Contains OPENAI_API_KEY


## 🧪 How to Use

### 1. Install dependencies

```bash
pip install -r requirements.txt
```


### 2. Add your OpenAI API key

Create a `.env` file:

OPENAI_API_KEY=your_key_here


3. ### Run the server

   python app/main.py


## 🧠 Model Used

* `gpt-4o` — OpenAI’s latest multimodal model
* Accepts both image and text input
* Returns structured invoice data (client name, invoice number, total, etc.)
