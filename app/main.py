from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, student, activity, question

# Cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API do projeto MIIA", version="1.0.0")

# Inclui as rotas
app.include_router(auth.router, tags=["Autenticação"])
app.include_router(student.router, tags=["Detalhes do Aluno"])
app.include_router(activity.router, tags=["Detalhes da Atividade"])
app.include_router(question.router, tags=["Detalhes da Questão"])
