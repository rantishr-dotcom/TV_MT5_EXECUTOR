import MetaTrader5 as mt5

from app.core.mt5_constants import (
    MAGIC_NUMBER,
    ORDER_COMMENT,
    DEFAULT_DEVIATION
)


def send_order(
    symbol,
    side,
    volume,
    sl,
    tp
):

    tick = mt5.symbol_info_tick(symbol)

    if tick is None:
        return None

    if side.upper() == "BUY":

        price = tick.ask
        order_type = mt5.ORDER_TYPE_BUY

    else:

        price = tick.bid
        order_type = mt5.ORDER_TYPE_SELL

    request = {

        "action": mt5.TRADE_ACTION_DEAL,

        "symbol": symbol,

        "volume": float(volume),

        "type": order_type,

        "price": float(price),

        "sl": float(sl),

        "tp": float(tp),

        "deviation": DEFAULT_DEVIATION,

        "magic": MAGIC_NUMBER,

        "comment": ORDER_COMMENT,

        "type_time": mt5.ORDER_TIME_GTC,

        "type_filling": mt5.ORDER_FILLING_IOC
    }

    print("=" * 50)
    print("ORDER REQUEST")
    print(request)

    result = mt5.order_send(request)

    print("=" * 50)
    print("ORDER RESULT")
    print(result)

    if result is not None:
        print("RETCODE =", result.retcode)
        print("COMMENT =", result.comment)

    return result