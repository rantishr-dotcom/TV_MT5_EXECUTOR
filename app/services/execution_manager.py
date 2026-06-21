
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
