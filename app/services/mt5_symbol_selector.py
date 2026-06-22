import MetaTrader5 as mt5


class MT5SymbolSelector:

    def ensure(
        self,
        symbol
    ):

        info = mt5.symbol_info(
            symbol
        )

        if info is None:
            return False

        if not info.visible:

            mt5.symbol_select(
                symbol,
                True
            )

        return True