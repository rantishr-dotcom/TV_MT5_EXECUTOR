from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():

    return {
        "database": "ok",
        "mt5": "ok",
        "webhook": "ok"
    }