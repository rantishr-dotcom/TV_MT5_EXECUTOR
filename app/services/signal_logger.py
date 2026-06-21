from sqlalchemy.orm import Session

from app.database.models import WebhookSignal


class SignalLogger:

    @staticmethod
    def save(db: Session, signal):

        row = WebhookSignal(
            symbol=signal.symbol,
            timeframe=signal.timeframe,
            side=signal.side,
            entry=signal.entry,
            sl=signal.sl,
            tp1=signal.tp1,
            tp2=signal.tp2,
            tp3=signal.tp3,
            score=signal.score,
            session=signal.session,
            mode=signal.mode
        )

        db.add(row)
        db.commit()

        return row