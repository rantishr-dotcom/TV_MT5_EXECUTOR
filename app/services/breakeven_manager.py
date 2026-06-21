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
        )\n