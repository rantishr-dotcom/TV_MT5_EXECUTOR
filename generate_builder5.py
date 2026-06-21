from pathlib import Path

BASE = Path.cwd()

FILES = {}

FILES["app/core/mt5_constants.py"] = '''
MAGIC_NUMBER = 555001

ORDER_COMMENT = "TV_MT5_EXECUTOR"

DEFAULT_DEVIATION = 20
'''

FILES["app/services/mt5_symbol_manager.py"] = '''
import MetaTrader5 as mt5


def ensure_symbol(symbol):

    info = mt5.symbol_info(symbol)

    if info is None:
        return False

    if not info.visible:
        mt5.symbol_select(symbol, True)

    return True
'''

FILES["app/services/mt5_position_manager.py"] = '''
import MetaTrader5 as mt5


def get_positions(symbol=None):

    if symbol:
        return mt5.positions_get(symbol=symbol)

    return mt5.positions_get()


def close_position(ticket):
    return ticket
'''

FILES["app/services/mt5_order_sender.py"] = '''
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

        "volume": volume,

        "type": order_type,

        "price": price,

        "sl": sl,

        "tp": tp,

        "deviation": DEFAULT_DEVIATION,

        "magic": MAGIC_NUMBER,

        "comment": ORDER_COMMENT,

        "type_time": mt5.ORDER_TIME_GTC,

        "type_filling": mt5.ORDER_FILLING_IOC

    }

    return mt5.order_send(request)
'''

FILES["app/services/mt5_trade_engine.py"] = '''
from app.services.mt5_symbol_manager import ensure_symbol

from app.services.mt5_order_sender import send_order

from app.services.risk_manager import calculate_lot_size


def execute_trade_signal(signal, balance=10000):

    if not ensure_symbol(signal.symbol):

        return {
            "success": False,
            "reason": "symbol not available"
        }

    lot = calculate_lot_size(
        balance,
        1,
        signal.entry,
        signal.sl
    )

    result = send_order(
        signal.symbol,
        signal.side,
        lot,
        signal.sl,
        signal.tp1
    )

    return {
        "success": True,
        "lot": lot,
        "result": str(result)
    }
'''

for file_path, content in FILES.items():

    full_path = BASE / file_path

    full_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    full_path.write_text(
        content.strip() + "\\n",
        encoding="utf-8"
    )

    print("Created:", file_path)

print("\\nBuilder #5 completed.")