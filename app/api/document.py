from fastapi import APIRouter

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("/health")
def health():
    return {"status": "Document service ready"}