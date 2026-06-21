from pathlib import Path

BASE = Path.cwd()

FILES = {}

FILES["app/database/signal_repository.py"] = '''
from sqlalchemy.orm import Session

from app.database.models import WebhookSignal


def save_signal(db: Session, signal_data: dict):

    signal = WebhookSignal(**signal_data)

    db.add(signal)

    db.commit()

    db.refresh(signal)

    return signal
'''

FILES["app/database/trade_repository.py"] = '''
def save_trade(db, trade):

    db.add(trade)

    db.commit()

    db.refresh(trade)

    return trade
'''

FILES["app/database/account_repository.py"] = '''
def get_account(db, account_id):

    return account_id
'''

FILES["app/services/signal_storage.py"] = '''
from app.database.signal_repository import save_signal


def store_signal(db, signal):

    return save_signal(
        db,
        signal.dict()
    )
'''

FILES["app/services/trade_storage.py"] = '''
from app.database.trade_repository import save_trade


def store_trade(db, trade):

    return save_trade(
        db,
        trade
    )
'''

FILES["app/api/signal_history.py"] = '''
from fastapi import APIRouter

router = APIRouter()


@router.get("/signals")

def signal_history():

    return {
        "status": "ready"
    }
'''

FILES["app/database/trade_history_models.py"] = '''
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
'''

FILES["app/database/webhook_log_models.py"] = '''
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
    )
'''

GENERATOR = '''
from app.database.db import Base
from app.database.db import engine

from app.database.models import *
from app.database.account_models import *
from app.database.group_models import *
from app.database.trade_models import *
from app.database.trade_history_models import *
from app.database.webhook_log_models import *


def create_all_tables():

    Base.metadata.create_all(bind=engine)

    print("All tables created.")
'''

FILES["app/database/create_all_tables.py"] = GENERATOR

for file_path, content in FILES.items():

    full_path = BASE / file_path

    full_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    full_path.write_text(
        content.strip() + "\\n",
        encoding="utf-8"
    )

    print("Created:", file_path)

print("\\nBuilder #6 completed.")