from pathlib import Path

BASE = Path.cwd()

FILES = {}

FILES["app/core/response_models.py"] = '''
def success_response(data=None):

    return {
        "success": True,
        "data": data
    }


def error_response(message):

    return {
        "success": False,
        "message": message
    }
'''

FILES["app/services/dashboard_service.py"] = '''
def get_dashboard_data():

    return {
        "accounts": 0,
        "signals": 0,
        "trades": 0,
        "open_positions": 0
    }
'''

FILES["app/services/statistics_service.py"] = '''
def get_statistics():

    return {
        "total_signals": 0,
        "total_trades": 0,
        "win_rate": 0
    }
'''

FILES["app/api/dashboard.py"] = '''
from fastapi import APIRouter

from app.services.dashboard_service import (
    get_dashboard_data
)

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    return get_dashboard_data()
'''

FILES["app/api/accounts.py"] = '''
from fastapi import APIRouter

router = APIRouter()


@router.get("/accounts")
def get_accounts():

    return {
        "accounts": []
    }


@router.post("/accounts")
def create_account():

    return {
        "status": "created"
    }


@router.delete("/accounts/{account_id}")
def delete_account(account_id: int):

    return {
        "deleted": account_id
    }
'''

FILES["app/api/trades.py"] = '''
from fastapi import APIRouter

router = APIRouter()


@router.get("/trades")
def trades():

    return {
        "trades": []
    }


@router.get("/trades/open")
def open_trades():

    return {
        "open": []
    }


@router.get("/trades/history")
def trade_history():

    return {
        "history": []
    }
'''

FILES["app/api/health.py"] = '''
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():

    return {
        "database": "ok",
        "mt5": "ok",
        "webhook": "ok"
    }
'''

GENERATOR_CODE = '''
from pathlib import Path

BASE = Path.cwd()

FILES = {}
'''

for path, content in FILES.items():

    full_path = BASE / path

    full_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    full_path.write_text(
        content.strip() + "\\n",
        encoding="utf-8"
    )

    print("Created:", path)

print("\\nBuilder #7 completed.")