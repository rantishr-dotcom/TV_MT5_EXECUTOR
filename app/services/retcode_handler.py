class RetcodeHandler:

    def parse(self, retcode):

        return {
            "retcode": retcode,
            "success": retcode == 10009
        }