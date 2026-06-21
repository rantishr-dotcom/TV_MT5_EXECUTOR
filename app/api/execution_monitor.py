from fastapi import APIRouter

router = APIRouter(
    prefix="/monitor",
    tags=["monitor"]
)


@router.get("/status")
def status():

    return {
        "status": "running"
    }\n