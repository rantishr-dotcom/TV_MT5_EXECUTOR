from fastapi import APIRouter

router = APIRouter()


@router.get("/execution/status")
def execution_status():
    return {
        "status": "running"
    }\n