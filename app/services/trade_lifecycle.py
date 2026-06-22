from app.services.tp_manager import (
    TPManager
)

from app.services.sl_manager import (
    SLManager
)

from app.services.trailing_engine import (
    TrailingEngine
)


class TradeLifecycle:

    def __init__(self):

        self.tp = TPManager()

        self.sl = SLManager()

        self.trailing = (
            TrailingEngine()
        )

    def process_tp1(
        self,
        trade
    ):

        return self.tp.tp1_hit(
            trade
        )

    def process_tp2(
        self,
        trade
    ):

        return self.tp.tp2_hit(
            trade
        )

    def process_tp3(
        self,
        trade
    ):

        return self.tp.tp3_hit(
            trade
        )