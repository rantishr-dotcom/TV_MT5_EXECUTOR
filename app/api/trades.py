from fastapi import APIRouter

router = APIRouter()


@router.get("/trades")
def trades():

    return {
        "trades": []
    }


@router.get("/trades/open")
def open_trades():

    return {
        "open": []
    }


@router.get("/trades/history")
def trade_history():

    return {
        "history": []
    }\n