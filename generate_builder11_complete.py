from pathlib import Path

FILES = {

"app/services/breakeven_manager.py": '''
import MetaTrader5 as mt5


class BreakevenManager:

    def move_to_breakeven(
        self,
        position
    ):

        request = {

            "action":
                mt5.TRADE_ACTION_SLTP,

            "position":
                position.ticket,

            "sl":
                position.price_open,

            "tp":
                position.tp
        }

        return mt5.order_send(
            request
        )
''',

"app/services/sl_manager.py": '''
import MetaTrader5 as mt5


class SLManager:

    def move_to_tp1(
        self,
        ticket,
        tp1_price
    ):

        request = {

            "action":
                mt5.TRADE_ACTION_SLTP,

            "position":
                ticket,

            "sl":
                tp1_price
        }

        return mt5.order_send(
            request
        )

    def move_to_be(
        self,
        ticket,
        entry
    ):

        request = {

            "action":
                mt5.TRADE_ACTION_SLTP,

            "position":
                ticket,

            "sl":
                entry
        }

        return mt5.order_send(
            request
        )
''',

"app/services/partial_close_manager.py": '''
import MetaTrader5 as mt5


class PartialCloseManager:

    def close_partial(
        self,
        position,
        percent
    ):

        volume = (
            position.volume *
            percent /
            100
        )

        request = {

            "action":
                mt5.TRADE_ACTION_DEAL,

            "symbol":
                position.symbol,

            "volume":
                volume,

            "position":
                position.ticket,

            "type":
                mt5.ORDER_TYPE_SELL
                if position.type == 0
                else mt5.ORDER_TYPE_BUY,

            "price":
                mt5.symbol_info_tick(
                    position.symbol
                ).bid
        }

        return mt5.order_send(
            request
        )
''',

"app/services/trailing_stop_manager.py": '''
import MetaTrader5 as mt5


class TrailingStopManager:

    def trail(
        self,
        position,
        new_sl
    ):

        current_sl = position.sl

        if new_sl <= current_sl:

            return None

        request = {

            "action":
                mt5.TRADE_ACTION_SLTP,

            "position":
                position.ticket,

            "sl":
                new_sl,

            "tp":
                position.tp
        }

        return mt5.order_send(
            request
        )
''',

"app/services/tp_manager.py": '''
class TPManager:

    def tp1_hit(
        self,
        trade
    ):

        trade["event"] = "tp1"

        return trade

    def tp2_hit(
        self,
        trade
    ):

        trade["event"] = "tp2"

        return trade

    def tp3_hit(
        self,
        trade
    ):

        trade["event"] = "tp3"

        return trade
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
        f"Updated: {file_path}"
    )

print("\\nBuilder11 Complete finished.")