from pathlib import Path
import shutil
from fastapi import HTTPException, UploadFile
import uuid
from app.core.logging import logger
from app.schemas.upload import UploadResponse
from app.services.pdf_services import extract_text

async def validate_pdf(file: UploadFile):

    logger.info(f"Validating file: {file.filename}")

    # Extension
    if not file.filename.lower().endswith(".pdf"):
        logger.warning(f"Invalid file extension: {file.filename}")

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Content-Type
    if file.content_type != "application/pdf":
        logger.warning(f"Invalid content type '{file.content_type}' for {file.filename}")
        raise HTTPException(
            status_code=400,
            detail="Invalid content type."
        )

    # Magic bytes
    header = await file.read(5)

    if header != b"%PDF-":
        logger.warning(f"Invalid PDF signature: {file.filename}")
        raise HTTPException(
            status_code=400,
            detail="Invalid PDF file."
        )
    logger.info("PDF validation successful")
    # Reset pointer
    await file.seek(0)


UPLOAD_DIR = Path("uploads")


async def save_pdf(file: UploadFile) -> UploadResponse:
    """
    Save the uploaded PDF to disk.
    """
    logger.info(f"Saving file: {file.filename}")

    UPLOAD_DIR.mkdir(exist_ok=True)

    extension = Path(file.filename).suffix

    document_id = str(uuid.uuid4())

    unique_filename = f"{uuid.uuid4()}{extension}"

    file_path = UPLOAD_DIR / unique_filename

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    except Exception as e:
        logger.error(f"Failed to save file: {e}")

        raise HTTPException(
            status_code=500,
            detail="Failed to save uploaded file."
        )
    logger.info(f"File saved successfully: {unique_filename}")
    return {
        "document_id": document_id,
        "original_filename": file.filename,
        "stored_filename": unique_filename,
        "file_path": file_path
    }

    