import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import get_db, Base
from app import models

# Banco de dados em memória para testes
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # ou sqlite:///:memory: se preferir

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação das tabelas no banco de teste
Base.metadata.create_all(bind=engine)

# Override da dependência do banco
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Substitui o banco de dados real pelo de teste
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture
def db_session():
    """Insere uma atividade de teste antes dos testes."""
    db = TestingSessionLocal()
    atividade = models.Activity(id=1, student_id=1, title="Atividade Teste", is_completed=False)
    db.add(atividade)
    db.commit()
    db.refresh(atividade)
    yield db
    db.close()

def test_get_activity(db_session):
    response = client.get("/activity/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Atividade Teste"

def test_patch_activity(db_session):
    data = { "id": 1, "student_id": 1, "title": "Atividade Teste" }
    response = client.patch("/activity/1", json=data)
    assert response.status_code == 200
    assert response.json()["is_completed"] is False

def test_post_complete_activity(db_session):
    data = { "id": 1, "student_id": 1, "title": "Atividade Teste" }
    response = client.post("/activity/1", json=data)
    assert response.status_code == 200
    assert response.json()["is_completed"] is True
