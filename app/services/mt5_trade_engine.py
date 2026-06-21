from app.services.mt5_symbol_manager import ensure_symbol

from app.services.mt5_order_sender import send_order

from app.services.risk_manager import calculate_lot_size


def execute_trade_signal(signal, balance=10000):

    if not ensure_symbol(signal.symbol):

        return {
            "success": False,
            "reason": "symbol not available"
        }

    lot = calculate_lot_size(
        balance,
        1,
        signal.entry,
        signal.sl
    )

    result = send_order(
        signal.symbol,
        signal.side,
        lot,
        signal.sl,
        signal.tp1
    )

    return {
        "success": True,
        "lot": lot,
        "result": str(result)
    }\n