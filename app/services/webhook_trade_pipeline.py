
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
