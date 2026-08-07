from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings
from app.api.upload import router as upload_router
from app.api.document import router as document_router


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
)

app.include_router(health_router)

app.include_router(upload_router)

app.include_router(document_router)


@app.get("/")
def root():
    return {"message": f"Welcome to {settings.app_name}"}