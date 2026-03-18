from fastapi import FastAPI
from app.routes import sum, subtract

app = FastAPI(title="Calculator API")

# Incluimos las rutas que vas a crear
app.include_router(sum.router)
app.include_router(subtract.router)

@app.get("/")
def read_root():
    return {"message": "API Calculadora"}