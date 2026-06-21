from pathlib import Path

FILES = {

"app/services/result_handler.py": '''
class ResultHandler:

    def process(
        self,
        result
    ):

        if result is None:

            return {
                "success": False,
                "reason": "no_result"
            }

        if isinstance(
            result,
            dict
        ):

            return result

        try:

            return {

                "success":
                    result.retcode == 10009,

                "retcode":
                    result.retcode,

                "comment":
                    getattr(
                        result,
                        "comment",
                        ""
                    ),

                "order":
                    getattr(
                        result,
                        "order",
                        0
                    )
            }

        except Exception as e:

            return {

                "success": False,
                "error": str(e)
            }
''',

"app/services/trade_state_manager.py": '''
class TradeStateManager:

    def create_state(
        self,
        ticket
    ):

        return {

            "ticket": ticket,
            "state": "OPEN"
        }

    def update_state(
        self,
        ticket,
        state
    ):

        return {

            "ticket": ticket,
            "state": state
        }
''',

"app/services/trade_storage.py": '''
from datetime import datetime


class TradeStorage:

    def store(
        self,
        signal,
        result
    ):

        return {

            "stored": True,

            "timestamp":
                datetime.utcnow().isoformat(),

            "symbol":
                signal.symbol,

            "side":
                signal.side,

            "result":
                result
        }
''',

"app/services/execution_manager.py": '''
from app.services.webhook_trade_pipeline import (
    WebhookTradePipeline
)

from app.services.trade_state_manager import (
    TradeStateManager
)

from app.services.trade_storage import (
    TradeStorage
)


class ExecutionManager:

    def __init__(self):

        self.pipeline = (
            WebhookTradePipeline()
        )

        self.state_manager = (
            TradeStateManager()
        )

        self.storage = (
            TradeStorage()
        )

    def run(
        self,
        signal
    ):

        result = self.pipeline.process(
            signal
        )

        ticket = 0

        if isinstance(
            result,
            dict
        ):

            ticket = result.get(
                "order",
                0
            )

        state = (
            self.state_manager.create_state(
                ticket
            )
        )

        stored = (
            self.storage.store(
                signal,
                result
            )
        )

        return {

            "result":
                result,

            "state":
                state,

            "stored":
                stored
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
        f"Updated: {file_path}"
    )

print("\\nBuilder10 Finish completed.")