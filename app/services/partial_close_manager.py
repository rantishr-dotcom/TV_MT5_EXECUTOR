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