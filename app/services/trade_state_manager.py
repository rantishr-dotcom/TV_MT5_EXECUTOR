
class TradeStateManager:

    def create_state(self, ticket):
        return {
            "ticket": ticket,
            "state": "OPEN"
        }

    def tp1_hit(self, trade):
        trade["state"] = "TP1"
        return trade

    def tp2_hit(self, trade):
        trade["state"] = "TP2"
        return trade

    def tp3_hit(self, trade):
        trade["state"] = "CLOSED"
        return trade

    def stoploss_hit(self, trade):
        trade["state"] = "STOPLOSS"
        return trade
