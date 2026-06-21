from sqlalchemy.orm import Session

from app.database.models import WebhookSignal


def save_signal(db: Session, signal_data: dict):

    signal = WebhookSignal(**signal_data)

    db.add(signal)

    db.commit()

    db.refresh(signal)

    return signal\n