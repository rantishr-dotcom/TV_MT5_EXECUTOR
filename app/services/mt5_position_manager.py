import MetaTrader5 as mt5


def get_positions(symbol=None):

    if symbol:
        return mt5.positions_get(symbol=symbol)

    return mt5.positions_get()


def close_position(ticket):
    return ticket