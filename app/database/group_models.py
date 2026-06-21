from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.db import Base


class AccountGroup(Base):

    __tablename__ = "account_groups"

    id = Column(Integer, primary_key=True)

    group_name = Column(String, unique=True)