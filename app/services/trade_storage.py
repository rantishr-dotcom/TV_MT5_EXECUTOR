
from datetime import datetime
from app.database.trade_repository import save_trade


def store_trade(db, trade):

    try:
        trade.created_at = datetime.utcnow()
    except Exception:
        pass

    return save_trade(
        db,
        trade
    )
