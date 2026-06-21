
def calculate_lot_size(
    balance,
    risk_percent,
    entry,
    sl,
    pip_value=10
):
    risk_amount = balance * (risk_percent / 100)

    stop_distance = abs(entry - sl)

    if stop_distance <= 0:
        return 0.0

    lot = risk_amount / (
        stop_distance * pip_value
    )

    return round(lot, 2)
