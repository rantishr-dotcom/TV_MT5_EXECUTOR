class CopyTradeManager:

    def copy_trade(
        self,
        master_trade
    ):
        return {
            "copied": True,
            "ticket": master_trade
        }\n