class TPManager:

    def tp1_hit(
        self,
        trade
    ):

        return {
            "ticket": trade.get("ticket"),
            "event": "tp1_hit"
        }

    def tp2_hit(
        self,
        trade
    ):

        return {
            "ticket": trade.get("ticket"),
            "event": "tp2_hit"
        }

    def tp3_hit(
        self,
        trade
    ):

        return {
            "ticket": trade.get("ticket"),
            "event": "tp3_hit"
        }\n