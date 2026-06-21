class SymbolMapper:

    MAP = {

        "XAUUSD":
            "XAUUSD",

        "US30":
            "US30",

        "NAS100":
            "NAS100"
    }

    def map(
        self,
        symbol
    ):
        return self.MAP.get(
            symbol,
            symbol
        )\n