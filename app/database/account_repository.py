from app.database.account_models import Account


class AccountRepository:

    @staticmethod
    def get_all(db):

        return db.query(Account).all()

    @staticmethod
    def get_active(db):

        return (
            db.query(Account)
            .filter(Account.is_active == True)
            .all()
        )