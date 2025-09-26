import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.mcp_server import toolkit
from src.utils.save_results import save_to_csv

def run_all_invoices():
    folder = "data/invoices"
    files = [f for f in os.listdir(folder) if f.endswith(".pdf")]

    output_rows = []

    for file_name in files:
        file_path = os.path.join(folder, file_name)
        input_payload = {
            "file_path": file_path,
            "file_name": file_name
        }

        result = toolkit.chain_tools(["extract_invoice", "validate_invoice"], input_payload)

        row = {
            "file_name": file_name,
            "client_name": result.get("client_name", ""),
            "invoice_amount": result.get("invoice_amount", ""),
            "product_name": result.get("product_name", ""),
            "valid": result.get("valid", ""),
            "reason": result.get("reason", "")
        }

        output_rows.append(row)

    save_to_csv(output_rows)

if __name__ == "__main__":
    run_all_invoices()
