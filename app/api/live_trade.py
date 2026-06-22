from fastapi import APIRouter

router = APIRouter()


@router.get("/live-trade/status")
def status():

    return {
        "live_trade": True
    }