from app.services.position_monitor import (
    PositionMonitor
)

from app.services.breakeven_manager import (
    BreakevenManager
)

from app.services.trailing_stop_manager import (
    TrailingStopManager
)

from app.services.partial_close_manager import (
    PartialCloseManager
)


class TradeManager:

    def __init__(self):

        self.monitor = PositionMonitor()

        self.breakeven = (
            BreakevenManager()
        )

        self.trailing = (
            TrailingStopManager()
        )

        self.partial = (
            PartialCloseManager()
        )

    def health(self):

        return {
            "positions":
                self.monitor.count()
        }\n