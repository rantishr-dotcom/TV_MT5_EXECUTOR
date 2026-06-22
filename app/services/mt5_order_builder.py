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