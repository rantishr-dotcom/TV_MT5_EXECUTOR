
from app.services.trade_pipeline import TradePipeline
from app.services.trade_state_manager import TradeStateManager


class ExecutionManager:

    def __init__(self):

        self.pipeline = TradePipeline()
        self.state_manager = TradeStateManager()

    def run(self, signal):

        result = self.pipeline.execute(
            signal
        )

        state = self.state_manager.create_state(
            ticket=0
        )

        return {
            "pipeline": result,
            "state": state
        }
