from pathlib import Path

BASE = Path(r"C:\Users\i_nan\OneDrive\Desktop\TV_MT5_EXECUTOR")

files = {}

files["app/services/mt5_manager.py"] = '''
import MetaTrader5 as mt5


class MT5Manager:

    def get_terminal_info(self):
        return mt5.terminal_info()

    def get_account_info(self):
        return mt5.account_info()

    def get_symbols(self):
        return mt5.symbols_get()
'''

files["app/services/account_manager.py"] = '''
import MetaTrader5 as mt5


class AccountManager:

    def current_account(self):
        return mt5.account_info()

    def current_terminal(self):
        return mt5.terminal_info()
'''

files["app/services/signal_logger.py"] = '''
from sqlalchemy.orm import Session

from app.database.models import WebhookSignal


class SignalLogger:

    @staticmethod
    def save(db: Session, signal):

        row = WebhookSignal(
            symbol=signal.symbol,
            timeframe=signal.timeframe,
            side=signal.side,
            entry=signal.entry,
            sl=signal.sl,
            tp1=signal.tp1,
            tp2=signal.tp2,
            tp3=signal.tp3,
            score=signal.score,
            session=signal.session,
            mode=signal.mode
        )

        db.add(row)
        db.commit()

        return row
'''

files["app/database/create_tables.py"] = '''
from app.database.db import engine
from app.database.models import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Database tables created.")
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

    print(f"Created: {filename}")

print("\\nBuilder #3 completed.")