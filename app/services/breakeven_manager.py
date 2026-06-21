class BreakevenManager:

    def move_to_breakeven(
        self,
        position
    ):

        return {
            "ticket": position.ticket,
            "action": "breakeven"
        }\n