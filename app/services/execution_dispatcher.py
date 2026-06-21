from app.services.account_router import AccountRouter


class ExecutionDispatcher:

    @staticmethod
    def dispatch(
        signal,
        accounts
    ):

        routed = AccountRouter.route(
            accounts
        )

        return {
            "signal": signal,
            "accounts": len(routed)
        }