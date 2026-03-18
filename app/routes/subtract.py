from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/subtract")
def calculate_subtract(num1: float, num2: float):
    return {
        "operation": "sum",
        "num1": num1,
        "num2": num2,
        "result": num1 - num2
    }