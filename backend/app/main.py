from fastapi import FastAPI
from app.api.health.db_test import router as db_router

app = FastAPI()

app.include_router(db_router)

@app.get("/health")
def health():
    return {"status": "ok"}