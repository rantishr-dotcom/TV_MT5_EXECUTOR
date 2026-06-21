from app.database.account_models import Account


class AccountRegistry:

    @staticmethod
    def create_account(
        db,
        account_number,
        broker,
        server,
        terminal_path
    ):

        account = Account(
            account_number=account_number,
            broker=broker,
            server=server,
            terminal_path=terminal_path
        )

        db.add(account)
        db.commit()

        return account