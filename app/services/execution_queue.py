class ExecutionQueue:

    def __init__(self):
        self.queue = []

    def add(
        self,
        signal
    ):
        self.queue.append(signal)

    def size(self):
        return len(self.queue)