from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/accounts/health"
)
def health():

    return {
        "status": "ok"
    }\n