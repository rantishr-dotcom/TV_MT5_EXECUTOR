class LotCalculator:

    def fixed_lot(
        self,
        lot_size
    ):
        return lot_size

    def risk_lot(
        self,
        balance,
        risk_percent,
        stop_loss_pips,
        pip_value=10
    ):

        risk_amount = (
            balance *
            risk_percent /
            100
        )

        if stop_loss_pips <= 0:
            return 0

        lot = (
            risk_amount /
            (
                stop_loss_pips *
                pip_value
            )
        )

        return round(
            lot,
            2
        )\n