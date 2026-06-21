class TrailingStopManager:

    def trail(
        self,
        position,
        distance
    ):

        return {
            "ticket": position.ticket,
            "distance": distance
        }\n