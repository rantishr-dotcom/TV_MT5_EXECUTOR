from pathlib import Path


FILES = {

    "app/services/lot_calculator.py": '''
class LotCalculator:

    def fixed_lot(
        self,
        lot_size
    ):
        return lot_size

    def risk_lot(
        self,
        balance,
        risk_percent,
        stop_loss_pips,
        pip_value=10
    ):

        risk_amount = (
            balance *
            risk_percent /
            100
        )

        if stop_loss_pips <= 0:
            return 0

        lot = (
            risk_amount /
            (
                stop_loss_pips *
                pip_value
            )
        )

        return round(
            lot,
            2
        )
''',

    "app/services/risk_engine.py": '''
from app.services.lot_calculator import LotCalculator


class RiskEngine:

    def __init__(self):

        self.calculator = LotCalculator()

    def calculate(
        self,
        mode,
        account,
        signal
    ):

        if mode == "fixed":

            return self.calculator.fixed_lot(
                account.fixed_lot
            )

        return self.calculator.risk_lot(
            account.balance,
            account.risk_percent,
            signal.stop_loss_pips
        )
''',

    "app/services/symbol_mapper.py": '''
class SymbolMapper:

    MAP = {

        "XAUUSD":
            "XAUUSD",

        "US30":
            "US30",

        "NAS100":
            "NAS100"
    }

    def map(
        self,
        symbol
    ):
        return self.MAP.get(
            symbol,
            symbol
        )
''',

    "app/services/trade_validator.py": '''
class TradeValidator:

    def validate(
        self,
        signal
    ):

        if signal.side not in [
            "BUY",
            "SELL"
        ]:
            return False

        if signal.entry <= 0:
            return False

        return True
''',

    "app/services/account_filter.py": '''
class AccountFilter:

    def enabled(
        self,
        account
    ):
        return account.enabled
''',

    "app/services/group_filter.py": '''
class GroupFilter:

    def enabled(
        self,
        group
    ):
        return group.enabled
''',

    "app/database/account_group_models.py": '''
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
''',

    "app/api/accounts_v2.py": '''
from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/accounts/health"
)
def health():

    return {
        "status": "ok"
    }
'''
}


for file_path, content in FILES.items():

    path = Path(file_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        content.strip() + "\\n",
        encoding="utf-8"
    )

    print(
        f"Created: {file_path}"
    )

print("\\nBuilder #8B completed.")