from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MCP Invoice Server is running"}

@app.post("/upload-invoice/")
async def upload_invoice(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return JSONResponse(status_code=400, content={"error": "Only PDF files are allowed."})
    
    # Save the uploaded file temporarily
    contents = await file.read()
    with open("temp_invoice.pdf", "wb") as f:
        f.write(contents)

    return {"message": "PDF received successfully", "filename": file.filename}
