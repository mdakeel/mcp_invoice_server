from parser import extract_text_from_pdf

pdf_path = "demo-invoice-20tax-2.pdf"  # Replace with your test file
text = extract_text_from_pdf(pdf_path)
print(text)
