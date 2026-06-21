import MetaTrader5 as mt5


class MT5Connector:

    def connect(self):

        if not mt5.initialize():
            return False

        return True

    def shutdown(self):
        mt5.shutdown()