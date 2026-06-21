class MultiAccountTradeEngine:

    def execute(self, signal, accounts):

        results = []

        for account in accounts:

            results.append({
                "account": account,
                "status": "queued"
            })

        return results\n