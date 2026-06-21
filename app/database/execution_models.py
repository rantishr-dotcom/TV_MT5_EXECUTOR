from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.db import Base


class ExecutionRecord(Base):

    __tablename__ = "execution_records"

    id = Column(Integer, primary_key=True)
    account = Column(String)
    status = Column(String)\n