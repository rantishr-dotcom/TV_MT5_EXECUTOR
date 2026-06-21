from pathlib import Path

BASE = Path(r"C:\Users\i_nan\OneDrive\Desktop\TV_MT5_EXECUTOR")

files = {}

files["app/core/config.py"] = '''
import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN", "tv_mt5_secret")

LIVE_TRADING = os.getenv(
    "LIVE_TRADING",
    "false"
).lower() == "true"
'''

files["app/services/risk_manager.py"] = '''
def calculate_lot_size(
    balance,
    risk_percent,
    entry,
    sl,
    pip_value=10
):
    risk_amount = balance * (risk_percent / 100)

    stop_distance = abs(entry - sl)

    if stop_distance <= 0:
        return 0.0

    lot = risk_amount / (
        stop_distance * pip_value
    )

    return round(lot, 2)
'''

files["app/services/trade_executor.py"] = '''
def execute_trade(signal):

    return {
        "status": "success",
        "symbol": signal.symbol,
        "side": signal.side
    }
'''

files["app/api/webhook.py"] = '''
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
'''

files["main.py"] = '''
from fastapi import FastAPI
from app.api.webhook import router

app = FastAPI(
    title="TV MT5 Executor"
)

app.include_router(router)
'''

for filepath, content in files.items():

    fullpath = BASE / filepath

    fullpath.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fullpath.write_text(
        content,
        encoding="utf-8"
    )

    print("Created:", filepath)

print("\\nBuilder #2 completed.")