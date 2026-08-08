from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.search_service import search_document

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = search_document(request.question)

    return ChatResponse(
        answer=result["answer"]
    )