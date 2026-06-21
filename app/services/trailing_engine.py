class TrailingEngine:

    def trail(
        self,
        current_sl,
        proposed_sl
    ):

        if proposed_sl <= current_sl:

            return current_sl

        return proposed_sl\n