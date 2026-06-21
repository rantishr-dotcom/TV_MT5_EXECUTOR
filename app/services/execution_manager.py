from app.services.trade_pipeline import (
    TradePipeline
)


class ExecutionManager:

    def __init__(self):

        self.pipeline = (
            TradePipeline()
        )

    def run(
        self,
        signal
    ):

        return self.pipeline.execute(
            signal
        )\n