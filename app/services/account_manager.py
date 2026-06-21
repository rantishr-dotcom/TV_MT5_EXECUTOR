import MetaTrader5 as mt5


class AccountManager:

    def current_account(self):
        return mt5.account_info()

    def current_terminal(self):
        return mt5.terminal_info()