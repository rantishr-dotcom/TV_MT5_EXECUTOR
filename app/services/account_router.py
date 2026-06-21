class AccountRouter:

    @staticmethod
    def route(accounts):

        active_accounts = []

        for account in accounts:

            if getattr(account, "is_active", False):

                active_accounts.append(account)

        return active_accounts