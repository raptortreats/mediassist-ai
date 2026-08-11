from fastapi import APIRouter

from app.services.document_service import list_documents

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("/health")
def health():
    return {"status": "Document service ready"}

@router.get("/")
def documents():
    return list_documents()