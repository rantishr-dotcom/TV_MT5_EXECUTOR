from fastapi import APIRouter

router = APIRouter()


@router.get("/accounts")
def get_accounts():

    return {
        "accounts": []
    }


@router.post("/accounts")
def create_account():

    return {
        "status": "created"
    }


@router.delete("/accounts/{account_id}")
def delete_account(account_id: int):

    return {
        "deleted": account_id
    }