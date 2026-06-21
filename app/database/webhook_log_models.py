from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.db import Base


class WebhookLog(Base):

    __tablename__ = "webhook_logs"

    id = Column(Integer, primary_key=True)

    symbol = Column(String)

    timeframe = Column(String)

    status = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )\n