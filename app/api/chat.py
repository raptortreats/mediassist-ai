from fastapi import APIRouter

from app.services.search_service import search_document

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.get("/")
def chat(query: str):

    results = search_document(query)

    return results