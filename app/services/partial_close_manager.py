class PartialCloseManager:

    def close_partial(
        self,
        position,
        percent
    ):

        return {
            "ticket": position.ticket,
            "closed_percent": percent
        }\n