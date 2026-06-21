from pathlib import Path

MAIN_PY = '''
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
app.include_router(monitor_router)
'''

WEBHOOK_PY = '''
from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.webhook import WebhookSignal

from app.core.config import WEBHOOK_TOKEN

from app.services.webhook_trade_pipeline import (
    WebhookTradePipeline
)

router = APIRouter()

pipeline = WebhookTradePipeline()


@router.post("/webhook")
def receive_signal(
    signal: WebhookSignal
):

    if signal.token != WEBHOOK_TOKEN:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    result = pipeline.process(
        signal
    )

    return {
        "received": True,
        "result": result
    }
'''

files = {
    "main.py": MAIN_PY,
    "app/api/webhook.py": WEBHOOK_PY
}

for file_path, content in files.items():

    path = Path(file_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        content.strip() + "\\n",
        encoding="utf-8"
    )

    print(
        f"Updated: {file_path}"
    )

print("\\nBuilder 9 Final Wire-Up completed.")