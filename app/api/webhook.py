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
    }\n