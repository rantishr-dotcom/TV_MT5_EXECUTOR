from pathlib import Path

FILES = {

    "app/services/mt5_live_connector.py": '''
import MetaTrader5 as mt5


class MT5LiveConnector:

    def connect(self):

        if not mt5.initialize():

            return False

        return True

    def shutdown(self):

        mt5.shutdown()

    def account_info(self):

        return mt5.account_info()

    def terminal_info(self):

        return mt5.terminal_info()
''',

    "app/services/mt5_symbol_selector.py": '''
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
''',

    "app/services/mt5_order_builder.py": '''
import MetaTrader5 as mt5


class MT5OrderBuilder:

    def build(
        self,
        signal,
        lot
    ):

        tick = mt5.symbol_info_tick(
            signal.symbol
        )

        if signal.side == "BUY":

            order_type = mt5.ORDER_TYPE_BUY

            price = tick.ask

        else:

            order_type = mt5.ORDER_TYPE_SELL

            price = tick.bid

        return {

            "action":
                mt5.TRADE_ACTION_DEAL,

            "symbol":
                signal.symbol,

            "volume":
                lot,

            "type":
                order_type,

            "price":
                price,

            "sl":
                signal.sl,

            "tp":
                signal.tp1,

            "comment":
                "TV_MT5_EXECUTOR",

            "type_time":
                mt5.ORDER_TIME_GTC,

            "type_filling":
                mt5.ORDER_FILLING_IOC
        }
''',

    "app/services/mt5_live_executor.py": '''
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
''',

    "app/api/mt5.py": '''
from fastapi import APIRouter

from app.services.mt5_live_connector import (
    MT5LiveConnector
)

router = APIRouter()


@router.get("/mt5/status")
def mt5_status():

    connector = (
        MT5LiveConnector()
    )

    return {

        "connected":
            connector.connect()
    }
'''
}


for file_path, content in FILES.items():

    path = Path(file_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        content.strip() + "\\n",
        encoding="utf-8"
    )

    print(
        f"Created: {file_path}"
    )

print("\\nBuilder #9 completed.")