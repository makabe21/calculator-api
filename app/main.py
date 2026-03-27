from fastapi import FastAPI
from app.routes import sum, subtract, multiply

app = FastAPI(title="Calculator API")

app.include_router(sum.router)
app.include_router(subtract.router)
app.include_router(multiply.router)  

@app.get("/")
def read_root():
    return {"message": "API Calculadora"}