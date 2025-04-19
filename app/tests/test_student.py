from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_student():
    response = client.post("/students/", json={
        "email": "test@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_get_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
