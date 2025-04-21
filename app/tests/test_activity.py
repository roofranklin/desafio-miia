from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_activity():
    # Primeiro cria um aluno para usar o ID
    student_resp = client.post("/students/", json={
        "email": "activityuser@example.com",
        "password": "123456"
    })
    student_id = student_resp.json()["id"]

    activity_data = {
        "name": "Atividade 1",
        "start_date": "2025-04-19T10:00:00",
        "duration": 60
    }

    response = client.post(f"/student/?id={student_id}", json=activity_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Atividade 1"

def test_get_activities():
    response = client.get("/activities/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
