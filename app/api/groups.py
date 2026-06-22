from fastapi import APIRouter

router = APIRouter()


@router.get("/groups")
def groups():
    return {
        "groups": []
    }