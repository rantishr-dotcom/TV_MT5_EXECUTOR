
from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.webhook import WebhookSignal
from app.services.trade_executor import execute_trade
from app.core.config import WEBHOOK_TOKEN

router = APIRouter()

@router.post("/webhook")
def receive_signal(signal: WebhookSignal):

    if signal.token != WEBHOOK_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    result = execute_trade(signal)

    return {
        "received": True,
        "result": result
    }
