def save_trade(db, trade):

    db.add(trade)

    db.commit()

    db.refresh(trade)

    return trade\n