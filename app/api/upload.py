from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import validate_pdf, save_pdf
from app.schemas.upload import UploadResponse
router = APIRouter()


@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    await validate_pdf(file)

    return await save_pdf(file)