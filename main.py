from fastapi import FastAPI

from app.api.webhook import router as webhook_router
from app.api.execution_monitor import router as monitor_router

app = FastAPI(
    title="TV MT5 Executor"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "application": "TV MT5 Executor"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

app.include_router(webhook_router)
app.include_router(monitor_router)\n