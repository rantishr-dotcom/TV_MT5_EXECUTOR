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