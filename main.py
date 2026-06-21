
from fastapi import FastAPI

app = FastAPI(
    title="TV MT5 Executor",
    version="1.0"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "project": "TV MT5 Executor"
    }

@app.get("/health")
def health():
    return {
        "api": "running"
    }
