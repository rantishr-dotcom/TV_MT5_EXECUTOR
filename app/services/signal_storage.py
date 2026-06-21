from app.database.signal_repository import save_signal


def store_signal(db, signal):

    return save_signal(
        db,
        signal.dict()
    )\n