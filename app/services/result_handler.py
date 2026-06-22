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