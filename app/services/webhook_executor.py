
from app.services.execution_manager import (
    ExecutionManager
)


class WebhookExecutor:

    def __init__(self):

        self.manager = (
            ExecutionManager()
        )

    def execute(
        self,
        signal
    ):

        return self.manager.run(
            signal
        )
