from fastapi import APIRouter


router = APIRouter(tags=["inference"])


@router.get("/")
def index():
    return {"message": "success"}
