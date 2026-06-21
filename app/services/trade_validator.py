class TradeValidator:

    def validate(
        self,
        signal
    ):

        if signal.side not in [
            "BUY",
            "SELL"
        ]:
            return False

        if signal.entry <= 0:
            return False

        return True\n