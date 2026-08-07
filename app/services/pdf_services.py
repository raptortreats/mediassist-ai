from pathlib import Path
import fitz


def extract_text(pdf_path: Path) -> str:
    """
    Extract all text from a PDF.
    """

    document = fitz.open(pdf_path)

    text = ""

    text_parts = []

    for page in document:
        text_parts.append(page.get_text())

    document.close()

    return "\n".join(text_parts)