
class ResultHandler:

    def process(self, result):

        if result is None:
            return {
                "success": False,
                "reason": "no_result"
            }

        try:

            return {
                "success": result.retcode == 10009,
                "retcode": result.retcode,
                "comment": getattr(result, "comment", "")
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }
