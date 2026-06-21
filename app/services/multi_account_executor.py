class MultiAccountExecutor:

    def execute(
        self,
        signal,
        accounts
    ):

        results = []

        for account in accounts:

            results.append({
                "account": account.account_number,
                "status": "queued"
            })

        return results