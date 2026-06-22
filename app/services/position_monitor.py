import MetaTrader5 as mt5


class PositionMonitor:

    def positions(self):

        return mt5.positions_get()

    def count(self):

        positions = mt5.positions_get()

        if positions is None:
            return 0

        return len(positions)