from app.services.signal_processor import (
    SignalProcessor
)


class TradePipeline:

    def __init__(self):

        self.processor = (
            SignalProcessor()
        )

    def execute(
        self,
        signal
    ):

        return self.processor.process(
            signal
        )\n