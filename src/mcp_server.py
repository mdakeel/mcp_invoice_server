from src.mcp_runtime import Toolkit
from src.tools.extract_invoice import extract_invoice_fields
from src.tools.validate_invoice import validate_invoice_fields

#initialize tool and registry
toolkit = Toolkit()
toolkit.add_tool(
    name="extract_invoice",
    description="Extract invoice fields using GPT",
    parameters={"file_path": "str", "file_name": "str"},
    returns={"client_name": "str", "invoice_amount": "float", "product_name": "str"},
    function=extract_invoice_fields
)

toolkit.add_tool(
    name="validate_invoice",
    description="Validate extracted invoice fields",
    parameters={"client_name": "str", "invoice_amount": "float", "product_name": "str"},
    returns={"valid": "bool", "reason": "str"},
    function=validate_invoice_fields
)
