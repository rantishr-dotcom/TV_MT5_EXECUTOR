from pathlib import Path

BASE = Path(r"C:\Users\i_nan\OneDrive\Desktop\TV_MT5_EXECUTOR")

files = {}

files["app/services/account_loader.py"] = '''
class AccountLoader:

    @staticmethod
    def load(accounts):

        return accounts
'''

files["app/services/account_router.py"] = '''
class AccountRouter:

    @staticmethod
    def route(accounts):

        active_accounts = []

        for account in accounts:

            if getattr(account, "is_active", False):

                active_accounts.append(account)

        return active_accounts
'''

files["app/services/account_health.py"] = '''
class AccountHealth:

    @staticmethod
    def check(account):

        return {
            "account": getattr(
                account,
                "account_number",
                "unknown"
            ),
            "healthy": True
        }
'''

files["app/services/execution_dispatcher.py"] = '''
from app.services.account_router import AccountRouter


class ExecutionDispatcher:

    @staticmethod
    def dispatch(
        signal,
        accounts
    ):

        routed = AccountRouter.route(
            accounts
        )

        return {
            "signal": signal,
            "accounts": len(routed)
        }
'''

files["app/database/account_service.py"] = '''
from app.database.account_repository import AccountRepository


class AccountService:

    @staticmethod
    def get_active_accounts(db):

        return AccountRepository.get_active(
            db
        )
'''

files["app/core/account_modes.py"] = '''
PAPER = "paper"

LIVE = "live"

MASTER = "master"

SLAVE = "slave"
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

print("\\nBuilder #4C completed.")