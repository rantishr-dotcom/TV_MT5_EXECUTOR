from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from app.database.db import Base


class TradeLog(Base):

    __tablename__ = "trade_logs"

    id = Column(Integer, primary_key=True)

    signal_id = Column(Integer)

    account_id = Column(Integer)

    symbol = Column(String)

    side = Column(String)

    lot = Column(Float)

    entry = Column(Float)

    sl = Column(Float)

    tp = Column(Float)

    ticket = Column(String)

    status = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )