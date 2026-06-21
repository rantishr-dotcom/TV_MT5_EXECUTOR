class AccountSelector:

    @staticmethod
    def get_active_accounts(accounts):

        return [
            x
            for x in accounts
            if x.is_active
        ]