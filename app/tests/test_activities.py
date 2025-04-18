from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_activity():
    response = client.post("/activities/", json={
        "student_id": 1,
        "start_time": "2025-04-18T08:00:00",
        "duration_minutes": 60
    })
    assert response.status_code in (200, 201)
    assert "id" in response.json()
