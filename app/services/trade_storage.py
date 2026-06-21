from app.database.trade_repository import save_trade


def store_trade(db, trade):

    return save_trade(
        db,
        trade
    )\n