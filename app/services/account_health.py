class AccountHealth:

    @staticmethod
    def check(account):

        return {
            "account": getattr(
                account,
                "account_number",
                "unknown"
            ),
            "healthy": True
        }