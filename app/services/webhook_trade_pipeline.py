
from app.services.signal_processor import SignalProcessor


class WebhookTradePipeline:

    def __init__(self):

        self.processor = SignalProcessor()

    def process(self, signal):

        return self.processor.process(
            signal
        )
