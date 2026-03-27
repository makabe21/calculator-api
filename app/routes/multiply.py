from fastapi import APIRouter

router = APIRouter()

@router.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    return {"resultado": a * b}