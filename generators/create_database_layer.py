from pathlib import Path

BASE = Path(r"C:\Users\i_nan\OneDrive\Desktop\TV_MT5_EXECUTOR")

database_dir = BASE / "app" / "database"
database_dir.mkdir(parents=True, exist_ok=True)

(database_dir / "__init__.py").write_text("")

(database_dir / "db.py").write_text(
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = (
    f"postgresql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
''',
encoding="utf-8"
)

(database_dir / "models.py").write_text(
'''
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from app.database.db import Base


class WebhookSignal(Base):

    __tablename__ = "webhook_signals"

    id = Column(Integer, primary_key=True, index=True)

    symbol = Column(String)

    timeframe = Column(String)

    side = Column(String)

    entry = Column(Float)

    sl = Column(Float)

    tp1 = Column(Float)

    tp2 = Column(Float)

    tp3 = Column(Float)

    score = Column(Integer)

    session = Column(String)

    mode = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
''',
encoding="utf-8"
)

print("DATABASE FILES CREATED")