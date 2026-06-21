
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from app.database.db import Base


class WebhookSignal(Base):

    __tablename__ = "webhook_signals"

    id = Column(Integer, primary_key=True, index=True)

    symbol = Column(String)

    timeframe = Column(String)

    side = Column(String)

    entry = Column(Float)

    sl = Column(Float)

    tp1 = Column(Float)

    tp2 = Column(Float)

    tp3 = Column(Float)

    score = Column(Integer)

    session = Column(String)

    mode = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
