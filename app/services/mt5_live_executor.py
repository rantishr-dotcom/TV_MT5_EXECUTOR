import MetaTrader5 as mt5

from app.services.mt5_order_builder import (
    MT5OrderBuilder
)

from app.services.mt5_symbol_selector import (
    MT5SymbolSelector
)


class MT5LiveExecutor:

    def __init__(self):

        self.builder = MT5OrderBuilder()

        self.selector = (
            MT5SymbolSelector()
        )

    def execute(
        self,
        signal,
        lot
    ):

        if not self.selector.ensure(
            signal.symbol
        ):

            return {
                "success": False,
                "reason": "symbol"
            }

        request = self.builder.build(
            signal,
            lot
        )

        result = mt5.order_send(
            request
        )

        return result