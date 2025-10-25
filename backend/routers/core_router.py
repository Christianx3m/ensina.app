from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=["🏠 Sistema"]
)

@router.get("/")
def root():
    return {"status": "Ensina.app backend online"}
