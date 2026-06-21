class TradeStateManager:

    def create_state(self, ticket):

        return {
            "ticket": ticket,
            "state": "OPEN"
        }\n