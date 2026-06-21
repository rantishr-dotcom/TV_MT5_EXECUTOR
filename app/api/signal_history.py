from fastapi import APIRouter

router = APIRouter()


@router.get("/signals")

def signal_history():

    return {
        "status": "ready"
    }\n