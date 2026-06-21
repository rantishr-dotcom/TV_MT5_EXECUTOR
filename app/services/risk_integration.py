from app.services.risk_manager import calculate_lot_size


class RiskIntegration:

    def calculate(
        self,
        balance,
        risk_percent,
        entry,
        sl
    ):

        return calculate_lot_size(
            balance,
            risk_percent,
            entry,
            sl
        )\n