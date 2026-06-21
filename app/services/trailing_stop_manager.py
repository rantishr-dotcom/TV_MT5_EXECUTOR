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
        )\n