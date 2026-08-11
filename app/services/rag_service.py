from pathlib import Path

from app.services.pdf_services import extract_text
from app.services.chunk_service import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.vector_store import add_documents


def process_document(pdf_path: Path, document_id: str, original_filename: str):
    """
    Complete RAG ingestion pipeline
    """

    text = extract_text(pdf_path)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    add_documents(chunks, embeddings, document_id, original_filename)

    return{
        "chunks": len(chunks),
        "status": "completed"
    }