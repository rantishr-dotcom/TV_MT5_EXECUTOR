from fastapi import APIRouter

from app.services.position_monitor import (
    PositionMonitor
)

router = APIRouter()


@router.get("/positions")

def positions():

    monitor = PositionMonitor()

    return {
        "count":
            monitor.count()
    }