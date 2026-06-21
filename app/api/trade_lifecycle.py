from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/trade-lifecycle/status"
)
def status():

    return {
        "status":
            "ready"
    }\n