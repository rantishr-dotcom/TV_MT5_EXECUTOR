class ResultHandler:

    def success(
        self,
        result
    ):

        return {
            "success": True,
            "result": result
        }

    def failure(
        self,
        reason
    ):

        return {
            "success": False,
            "reason": reason
        }\n