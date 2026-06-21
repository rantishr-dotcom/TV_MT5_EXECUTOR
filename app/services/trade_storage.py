from datetime import datetime


class TradeStorage:

    def store(
        self,
        signal,
        result
    ):

        return {

            "stored": True,

            "timestamp":
                datetime.utcnow().isoformat(),

            "symbol":
                signal.symbol,

            "side":
                signal.side,

            "result":
                result
        }\n