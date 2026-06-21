from pathlib import Path

BASE = Path("app/services")

# TradeStateManager
(BASE / "trade_state_manager.py").write_text("""
class TradeStateManager:

    def create_state(self, ticket):
        return {
            "ticket": ticket,
            "state": "OPEN"
        }

    def tp1_hit(self, trade):
        trade["state"] = "TP1"
        return trade

    def tp2_hit(self, trade):
        trade["state"] = "TP2"
        return trade

    def tp3_hit(self, trade):
        trade["state"] = "CLOSED"
        return trade

    def stoploss_hit(self, trade):
        trade["state"] = "STOPLOSS"
        return trade
""")

# ResultHandler
(BASE / "result_handler.py").write_text("""
class ResultHandler:

    def process(self, result):

        if result is None:
            return {
                "success": False,
                "reason": "no_result"
            }

        try:

            return {
                "success": result.retcode == 10009,
                "retcode": result.retcode,
                "comment": getattr(result, "comment", "")
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }
""")

# TradeManager
(BASE / "trade_manager.py").write_text("""
from app.services.position_monitor import PositionMonitor
from app.services.breakeven_manager import BreakevenManager
from app.services.trailing_stop_manager import TrailingStopManager
from app.services.partial_close_manager import PartialCloseManager


class TradeManager:

    def __init__(self):

        self.monitor = PositionMonitor()
        self.breakeven = BreakevenManager()
        self.trailing = TrailingStopManager()
        self.partial = PartialCloseManager()

    def monitor_positions(self):
        return self.monitor.positions()

    def move_breakeven(self, position):
        return self.breakeven.move_to_breakeven(position)

    def trail_position(self, position, distance):
        return self.trailing.trail(position, distance)

    def partial_close(self, position, percent):
        return self.partial.close_partial(position, percent)

    def health(self):
        return {
            "positions": self.monitor.count()
        }
""")

# TradeStorage
(BASE / "trade_storage.py").write_text("""
from datetime import datetime
from app.database.trade_repository import save_trade


def store_trade(db, trade):

    try:
        trade.created_at = datetime.utcnow()
    except Exception:
        pass

    return save_trade(
        db,
        trade
    )
""")

# TradePipeline
(BASE / "trade_pipeline.py").write_text("""
from app.services.signal_processor import SignalProcessor


class TradePipeline:

    def __init__(self):

        self.processor = SignalProcessor()

    def execute(self, signal):

        return self.processor.process(
            signal
        )
""")

# ExecutionManager
(BASE / "execution_manager.py").write_text("""
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
""")

# WebhookExecutor
(BASE / "webhook_executor.py").write_text("""
from app.services.execution_manager import ExecutionManager


class WebhookExecutor:

    def __init__(self):

        self.manager = ExecutionManager()

    def execute(self, signal):

        return self.manager.run(
            signal
        )
""")

# WebhookTradePipeline
(BASE / "webhook_trade_pipeline.py").write_text("""
from app.services.signal_processor import SignalProcessor


class WebhookTradePipeline:

    def __init__(self):

        self.processor = SignalProcessor()

    def process(self, signal):

        return self.processor.process(
            signal
        )
""")

print("\\nBuilder10 Complete generated.")