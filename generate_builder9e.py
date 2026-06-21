from pathlib import Path

FILES = {

    "app/services/tp_manager.py": '''
class TPManager:

    def tp1_hit(
        self,
        trade
    ):

        return {
            "ticket": trade.get("ticket"),
            "event": "tp1_hit"
        }

    def tp2_hit(
        self,
        trade
    ):

        return {
            "ticket": trade.get("ticket"),
            "event": "tp2_hit"
        }

    def tp3_hit(
        self,
        trade
    ):

        return {
            "ticket": trade.get("ticket"),
            "event": "tp3_hit"
        }
''',

    "app/services/sl_manager.py": '''
class SLManager:

    def move_to_tp1(
        self,
        ticket,
        tp1_price
    ):

        return {
            "ticket": ticket,
            "new_sl": tp1_price
        }

    def move_to_be(
        self,
        ticket,
        entry
    ):

        return {
            "ticket": ticket,
            "new_sl": entry
        }
''',

    "app/services/trailing_engine.py": '''
class TrailingEngine:

    def trail(
        self,
        current_sl,
        proposed_sl
    ):

        if proposed_sl <= current_sl:

            return current_sl

        return proposed_sl
''',

    "app/services/trade_lifecycle.py": '''
from app.services.tp_manager import (
    TPManager
)

from app.services.sl_manager import (
    SLManager
)

from app.services.trailing_engine import (
    TrailingEngine
)


class TradeLifecycle:

    def __init__(self):

        self.tp = TPManager()

        self.sl = SLManager()

        self.trailing = (
            TrailingEngine()
        )

    def process_tp1(
        self,
        trade
    ):

        return self.tp.tp1_hit(
            trade
        )

    def process_tp2(
        self,
        trade
    ):

        return self.tp.tp2_hit(
            trade
        )

    def process_tp3(
        self,
        trade
    ):

        return self.tp.tp3_hit(
            trade
        )
''',

    "app/api/trade_lifecycle.py": '''
from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/trade-lifecycle/status"
)
def status():

    return {
        "status":
            "ready"
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

print("\\nBuilder #9E completed.")