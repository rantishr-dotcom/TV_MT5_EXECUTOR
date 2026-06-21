from pathlib import Path

BASE = Path(r"C:\Users\i_nan\OneDrive\Desktop\TV_MT5_EXECUTOR")

files = {}

files["app/database/account_models.py"] = '''
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
'''

files["app/database/group_models.py"] = '''
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.db import Base


class AccountGroup(Base):

    __tablename__ = "account_groups"

    id = Column(Integer, primary_key=True)

    group_name = Column(String, unique=True)
'''

files["app/database/trade_models.py"] = '''
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
'''

files["app/services/trade_logger.py"] = '''
class TradeLogger:

    @staticmethod
    def log_trade(data):
        return data
'''

files["app/services/mt5_connector.py"] = '''
import MetaTrader5 as mt5


class MT5Connector:

    def connect(self):

        if not mt5.initialize():
            return False

        return True

    def shutdown(self):
        mt5.shutdown()
'''

for filename, content in files.items():

    full = BASE / filename

    full.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    full.write_text(
        content.strip(),
        encoding="utf-8"
    )

    print("Created:", filename)

print("\\nBuilder #4 Part A completed.")