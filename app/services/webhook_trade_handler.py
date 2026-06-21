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
        )\n