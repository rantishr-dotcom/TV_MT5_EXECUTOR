from pathlib import Path

FILES = {

    "app/services/live_trade_service.py": '''
from app.services.trade_validator import TradeValidator
from app.services.lot_calculator import LotCalculator
from app.services.mt5_live_executor import MT5LiveExecutor


class LiveTradeService:

    def __init__(self):

        self.validator = TradeValidator()
        self.calculator = LotCalculator()
        self.executor = MT5LiveExecutor()

    def execute(
        self,
        signal
    ):

        valid = self.validator.validate(
            signal
        )

        if not valid:

            return {
                "success": False,
                "reason": "validation"
            }

        lot = 0.01

        result = self.executor.execute(
            signal,
            lot
        )

        return {
            "success": True,
            "lot": lot,
            "result": str(result)
        }
''',

    "app/services/webhook_trade_handler.py": '''
from app.services.live_trade_service import (
    LiveTradeService
)


class WebhookTradeHandler:

    def __init__(self):

        self.service = (
            LiveTradeService()
        )

    def handle(
        self,
        signal
    ):

        return self.service.execute(
            signal
        )
''',

    "app/api/live_trade.py": '''
from fastapi import APIRouter

router = APIRouter()


@router.get("/live-trade/status")
def status():

    return {
        "live_trade": True
    }
'''
}


for file_path, content in FILES.items():

    path = Path(file_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        content.strip() + "\\n",
        encoding="utf-8"
    )

    print(f"Created: {file_path}")

print("\\nBuilder #9C completed.")