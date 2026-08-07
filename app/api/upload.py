from pathlib import Path
from app.services.rag_service import process_document
from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import validate_pdf, save_pdf
from app.schemas.upload import UploadResponse
router = APIRouter()


@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    await validate_pdf(file)

    upload_response = await save_pdf(file)

    process_document(
        Path("uploads") / upload_response["stored_filename"]   

    )

    return UploadResponse(

        message="File uploaded successfully",
        original_filename=upload_response["original_filename"],
        stored_filename=upload_response["stored_filename"],
    )