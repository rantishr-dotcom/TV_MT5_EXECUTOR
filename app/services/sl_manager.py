class SLManager:

    def move_to_tp1(
        self,
        ticket,
        tp1_price
    ):

        return {
            "ticket": ticket,
            "new_sl": tp1_price
        }

    def move_to_be(
        self,
        ticket,
        entry
    ):

        return {
            "ticket": ticket,
            "new_sl": entry
        }\n