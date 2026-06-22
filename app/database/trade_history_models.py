from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from app.database.db import Base


class TradeHistory(Base):

    __tablename__ = "trade_history"

    id = Column(Integer, primary_key=True)

    symbol = Column(String)

    side = Column(String)

    volume = Column(Float)

    profit = Column(Float)

    account_name = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )