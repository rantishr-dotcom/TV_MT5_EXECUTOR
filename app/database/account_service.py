from app.database.account_repository import AccountRepository


class AccountService:

    @staticmethod
    def get_active_accounts(db):

        return AccountRepository.get_active(
            db
        )