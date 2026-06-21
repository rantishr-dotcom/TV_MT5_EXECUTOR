from pathlib import Path

BASE = Path(r"C:\Users\i_nan\OneDrive\Desktop\TV_MT5_EXECUTOR")

files = {}

files["app/services/account_registry.py"] = '''
from app.database.account_models import Account


class AccountRegistry:

    @staticmethod
    def create_account(
        db,
        account_number,
        broker,
        server,
        terminal_path
    ):

        account = Account(
            account_number=account_number,
            broker=broker,
            server=server,
            terminal_path=terminal_path
        )

        db.add(account)
        db.commit()

        return account
'''

files["app/services/account_selector.py"] = '''
class AccountSelector:

    @staticmethod
    def get_active_accounts(accounts):

        return [
            x
            for x in accounts
            if x.is_active
        ]
'''

files["app/services/multi_account_executor.py"] = '''
class MultiAccountExecutor:

    def execute(
        self,
        signal,
        accounts
    ):

        results = []

        for account in accounts:

            results.append({
                "account": account.account_number,
                "status": "queued"
            })

        return results
'''

files["app/database/account_repository.py"] = '''
from app.database.account_models import Account


class AccountRepository:

    @staticmethod
    def get_all(db):

        return db.query(Account).all()

    @staticmethod
    def get_active(db):

        return (
            db.query(Account)
            .filter(Account.is_active == True)
            .all()
        )
'''

files["app/core/constants.py"] = '''
DEFAULT_RISK_PERCENT = 1.0

SUPPORTED_MODES = [
    "paper",
    "live"
]

SUPPORTED_SIDES = [
    "BUY",
    "SELL"
]
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

print("\\nBuilder #4 Part B completed.")