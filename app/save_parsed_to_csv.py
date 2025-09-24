import os
import csv
from image_agent import parse_invoice_image

folder = "invoices"
output_csv = "parsed_invoices.csv"

# Define CSV headers
headers = ["filename", "client_name", "invoice_number", "total_amount"]

with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()

    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(folder, filename)
            parsed = parse_invoice_image(path)

            writer.writerow({
                "filename": filename,
                "client_name": parsed.get("client_name", ""),
                "invoice_number": parsed.get("invoice_number", ""),
                "total_amount": parsed.get("total_amount", "")
            })

print(f"Saved parsed results to {output_csv}")
