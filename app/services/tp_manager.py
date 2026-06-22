class TPManager:

    def tp1_hit(
        self,
        trade
    ):

        trade["event"] = "tp1"

        return trade

    def tp2_hit(
        self,
        trade
    ):

        trade["event"] = "tp2"

        return trade

    def tp3_hit(
        self,
        trade
    ):

        trade["event"] = "tp3"

        return trade