from pathlib import Path

Path("app/services/webhook_trade_pipeline.py").write_text("""
from app.services.signal_processor import SignalProcessor
from app.services.mt5_trade_engine import execute_trade_signal
from app.services.result_handler import ResultHandler


class WebhookTradePipeline:

    def __init__(self):

        self.processor = SignalProcessor()
        self.handler = ResultHandler()

    def process(self, signal):

        processed = self.processor.process(
            signal
        )

        if not processed.get("valid"):

            return {
                "success": False,
                "reason": "validation_failed"
            }

        result = execute_trade_signal(
            signal
        )

        return self.handler.process(
            result
        )
""")

Path("app/services/execution_manager.py").write_text("""
from app.services.webhook_trade_pipeline import (
    WebhookTradePipeline
)

from app.services.trade_state_manager import (
    TradeStateManager
)


class ExecutionManager:

    def __init__(self):

        self.pipeline = (
            WebhookTradePipeline()
        )

        self.state_manager = (
            TradeStateManager()
        )

    def run(
        self,
        signal
    ):

        result = self.pipeline.process(
            signal
        )

        state = self.state_manager.create_state(
            ticket=0
        )

        return {
            "result": result,
            "state": state
        }
""")

Path("app/services/webhook_executor.py").write_text("""
from app.services.execution_manager import (
    ExecutionManager
)


class WebhookExecutor:

    def __init__(self):

        self.manager = (
            ExecutionManager()
        )

    def execute(
        self,
        signal
    ):

        return self.manager.run(
            signal
        )
""")

print("Builder10 Final completed.")