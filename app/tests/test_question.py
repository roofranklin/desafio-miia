from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_question_objective():
    # Cria um aluno e uma atividade primeiro
    student_resp = client.post("/students/", json={
        "email": "questionuser@example.com",
        "password": "123456"
    })
    student_id = student_resp.json()["id"]

    activity_resp = client.post("/activities/?student_id=" + str(student_id), json={
        "name": "Atividade Questão",
        "start_date": "2025-04-19T12:00:00",
        "duration": 45
    })
    activity_id = activity_resp.json()["id"]

    question_data = {
        "type": "objetiva",
        "statement": "Qual a capital da França?",
        "objective_options": [
            {"option": "Paris", "is_correct": True, "student_answer": False},
            {"option": "Londres", "is_correct": False, "student_answer": False}
        ]
    }

    response = client.post(f"/questions/?activity_id={activity_id}", json=question_data)
    assert response.status_code == 200
    assert response.json()["statement"] == "Qual a capital da França?"

def test_get_questions():
    response = client.get("/questions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
