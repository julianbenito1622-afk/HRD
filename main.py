from fastapi import FastAPI
from src.core.config import init_db

app = FastAPI(title="HRD - Home Router Daemon", version="0.1.0")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"message": "HRD funcionando", "version": "0.1.0"}

@app.get("/health")
def health():
    return {"status": "ok"}