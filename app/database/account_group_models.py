from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

from app.database.db import Base


class AccountGroup(Base):

    __tablename__ = "account_groups"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    enabled = Column(
        Boolean,
        default=True
    )