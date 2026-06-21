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
        )\n