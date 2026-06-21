class GroupExecutor:

    def execute_group(
        self,
        group_name,
        signal
    ):
        return {
            "group": group_name,
            "status": "queued"
        }\n