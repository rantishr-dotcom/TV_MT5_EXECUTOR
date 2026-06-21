from fastapi import APIRouter

from app.services.mt5_live_connector import (
    MT5LiveConnector
)

router = APIRouter()


@router.get("/mt5/status")
def mt5_status():

    connector = (
        MT5LiveConnector()
    )

    return {

        "connected":
            connector.connect()
    }\n