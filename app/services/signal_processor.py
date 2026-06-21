from app.services.trade_validator import (
    TradeValidator
)


class SignalProcessor:

    def __init__(self):

        self.validator = (
            TradeValidator()
        )

    def process(
        self,
        signal
    ):

        valid = self.validator.validate(
            signal
        )

        return {
            "valid": valid,
            "signal": signal
        }\n