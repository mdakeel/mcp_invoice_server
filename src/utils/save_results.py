import os
import csv

def save_to_csv(rows: list, output_path="output/invoice_results.csv"):
    if not rows:
        print(" No data to save.")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Results saved to {output_path}")
