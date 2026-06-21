from pathlib import Path

FILES = {

    "app/services/breakeven_manager.py": '''
class BreakevenManager:

    def move_to_breakeven(
        self,
        position
    ):

        return {
            "ticket": position.ticket,
            "action": "breakeven"
        }
''',

    "app/services/trailing_stop_manager.py": '''
class TrailingStopManager:

    def trail(
        self,
        position,
        distance
    ):

        return {
            "ticket": position.ticket,
            "distance": distance
        }
''',

    "app/services/partial_close_manager.py": '''
class PartialCloseManager:

    def close_partial(
        self,
        position,
        percent
    ):

        return {
            "ticket": position.ticket,
            "closed_percent": percent
        }
''',

    "app/services/position_monitor.py": '''
import MetaTrader5 as mt5


class PositionMonitor:

    def positions(self):

        return mt5.positions_get()

    def count(self):

        positions = mt5.positions_get()

        if positions is None:
            return 0

        return len(positions)
''',

    "app/services/trade_manager.py": '''
from app.services.position_monitor import (
    PositionMonitor
)

from app.services.breakeven_manager import (
    BreakevenManager
)

from app.services.trailing_stop_manager import (
    TrailingStopManager
)

from app.services.partial_close_manager import (
    PartialCloseManager
)


class TradeManager:

    def __init__(self):

        self.monitor = PositionMonitor()

        self.breakeven = (
            BreakevenManager()
        )

        self.trailing = (
            TrailingStopManager()
        )

        self.partial = (
            PartialCloseManager()
        )

    def health(self):

        return {
            "positions":
                self.monitor.count()
        }
''',

    "app/api/positions.py": '''
from fastapi import APIRouter

from app.services.position_monitor import (
    PositionMonitor
)

router = APIRouter()


@router.get("/positions")

def positions():

    monitor = PositionMonitor()

    return {
        "count":
            monitor.count()
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

print("\\nBuilder #9D completed.")