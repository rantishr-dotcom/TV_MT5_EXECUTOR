from app.services.lot_calculator import LotCalculator


class RiskEngine:

    def __init__(self):

        self.calculator = LotCalculator()

    def calculate(
        self,
        mode,
        account,
        signal
    ):

        if mode == "fixed":

            return self.calculator.fixed_lot(
                account.fixed_lot
            )

        return self.calculator.risk_lot(
            account.balance,
            account.risk_percent,
            signal.stop_loss_pips
        )