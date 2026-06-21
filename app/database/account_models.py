from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from datetime import datetime

from app.database.db import Base


class Account(Base):

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)

    account_number = Column(String, unique=True)

    broker = Column(String)

    server = Column(String)

    terminal_path = Column(String)

    is_active = Column(Boolean, default=True)

    is_master = Column(Boolean, default=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )