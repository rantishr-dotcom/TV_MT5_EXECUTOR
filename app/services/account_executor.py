class AccountExecutor:

    def execute(
        self,
        account,
        signal
    ):
        return {
            "account": account,
            "status": "queued",
            "symbol": signal.symbol
        }