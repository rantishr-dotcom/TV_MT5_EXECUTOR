from app.services.webhook_trade_pipeline import (
    WebhookTradePipeline
)

from app.services.trade_state_manager import (
    TradeStateManager
)

from app.services.trade_storage import (
    TradeStorage
)


class ExecutionManager:

    def __init__(self):

        self.pipeline = (
            WebhookTradePipeline()
        )

        self.state_manager = (
            TradeStateManager()
        )

        self.storage = (
            TradeStorage()
        )

    def run(
        self,
        signal
    ):

        result = self.pipeline.process(
            signal
        )

        ticket = 0

        if isinstance(
            result,
            dict
        ):

            ticket = result.get(
                "order",
                0
            )

        state = (
            self.state_manager.create_state(
                ticket
            )
        )

        stored = (
            self.storage.store(
                signal,
                result
            )
        )

        return {

            "result":
                result,

            "state":
                state,

            "stored":
                stored
        }