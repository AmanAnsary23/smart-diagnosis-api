from fastapi import FastAPI
from routes.diagnosis import router

app = FastAPI(
    title="Smart Diagnosis API",
    description="AI-powered medical diagnosis API using Gemini",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Smart Diagnosis API is running!"}