import MetaTrader5 as mt5


class MT5Manager:

    def get_terminal_info(self):
        return mt5.terminal_info()

    def get_account_info(self):
        return mt5.account_info()

    def get_symbols(self):
        return mt5.symbols_get()