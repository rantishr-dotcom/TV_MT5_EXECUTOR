import MetaTrader5 as mt5


def ensure_symbol(symbol):

    info = mt5.symbol_info(symbol)

    if info is None:
        return False

    if not info.visible:
        mt5.symbol_select(symbol, True)

    return True\n