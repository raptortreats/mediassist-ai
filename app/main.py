from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="MediAssist AI",
    description="AI-powered medical research assistant",
    version="0.1.0"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "Welcome to MediAssist AI"}