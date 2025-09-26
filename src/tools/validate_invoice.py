# src/tools/validate_invoice.py

def validate_invoice_fields(client_name: str, invoice_amount: float, product_name: str, **kwargs):
    if not client_name or not isinstance(client_name, str):
        return {"valid": False, "reason": "Missing or invalid client name"}

    if not isinstance(invoice_amount, (int, float)) or invoice_amount <= 0:
        return {"valid": False, "reason": "Invalid invoice amount"}

    if not product_name or not isinstance(product_name, (str, list)):
        return {"valid": False, "reason": "Missing or invalid product name"}

    return {"valid": True, "reason": "Invoice looks good"}

