from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_multiplicacion():
    response = client.get("/multiplicar/2/3")
    assert response.status_code == 200
    assert response.json() == {"resultado": 6}