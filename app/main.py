from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to MediAssist AI"}

@app.get("/health")
def health_check():
    return{
        "status": "healthy",
        "application": "MediAssist AI"
    }