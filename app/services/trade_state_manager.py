class TradeStateManager:

    def create_state(
        self,
        ticket
    ):

        return {

            "ticket": ticket,
            "state": "OPEN"
        }

    def update_state(
        self,
        ticket,
        state
    ):

        return {

            "ticket": ticket,
            "state": state
        }\n