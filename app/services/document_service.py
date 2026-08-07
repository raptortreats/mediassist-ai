from pathlib import Path

from app.services.pdf_service import extract_text


def process_pdf(pdf_path: Path) -> str:
    """
    Process an uploaded PDF and return extracted text.
    """

    text = extract_text(pdf_path)

    return text