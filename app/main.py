import os
# from parser import extract_text_from_pdf
# from mcp_agent import parse_with_chatgpt


#text send to gpt

invoice_folder = "invoices"
summary = []

# for filename in os.listdir(invoice_folder):
#     if filename.endswith(".pdf"):
#         path = os.path.join(invoice_folder, filename)
#         text = extract_text_from_pdf(path)
#         parsed = parse_with_chatgpt(text)

#         summary.append({
#             "filename": filename,
#             "parsed": parsed
#         })

# # Print summary
# for item in summary:
#     print(f"\n{item['filename']}")
#     print(item['parsed'])



#Image send to gpt

from image_agent import parse_invoice_image


for filename in os.listdir(invoice_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(invoice_folder, filename)
        parsed = parse_invoice_image(path)

        summary.append({
            "filename": filename,
            "parsed": parsed
        })

# Print summary
for item in summary:
    print(f"\n{item['filename']}")
    print(item['parsed'])

