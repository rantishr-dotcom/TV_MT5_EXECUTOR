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