from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.db import Base


class CopyTrade(Base):

    __tablename__ = "copy_trades"

    id = Column(Integer, primary_key=True)
    master_ticket = Column(String)\n