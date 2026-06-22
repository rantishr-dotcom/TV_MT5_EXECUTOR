import MetaTrader5 as mt5

from app.services.mt5_symbol_manager import ensure_symbol
from app.services.mt5_order_sender import send_order
from app.services.risk_manager import calculate_lot_size


def execute_trade_signal(signal, balance=10000):

    try:

        init_ok = mt5.initialize()

        print("=" * 50)
        print("MT5 INIT =", init_ok)
        print("SIGNAL SYMBOL =", repr(signal.symbol))
        print("SIGNAL SIDE =", signal.side)

        if not init_ok:
            return {
                "success": False,
                "reason": "mt5_init_failed"
            }

        info = mt5.symbol_info(signal.symbol)

        print("SYMBOL INFO =", info)

        symbol_ok = ensure_symbol(signal.symbol)

        print("ENSURE_SYMBOL =", symbol_ok)

        if not symbol_ok:
            return {
                "success": False,
                "reason": "symbol_not_available",
                "symbol": signal.symbol
            }

        lot = calculate_lot_size(
            balance,
            1,
            signal.entry,
            signal.sl
        )

        print("LOT =", lot)

        result = send_order(
            signal.symbol,
            signal.side,
            lot,
            signal.sl,
            signal.tp1
        )

        print("ORDER RESULT =", result)

        if result is None:
            return {
                "success": False,
                "reason": "order_send_returned_none"
            }

        return {
            "success": True,
            "lot": lot,
            "retcode": getattr(result, "retcode", None),
            "order": getattr(result, "order", None),
            "deal": getattr(result, "deal", None),
            "comment": getattr(result, "comment", "")
        }

    except Exception as e:

        return {
            "success": False,
            "reason": str(e)
        }

    finally:

        try:
            mt5.shutdown()
        except Exception:
            pass