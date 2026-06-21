
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
