from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, student, activity, question

# Cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API do projeto MIIA", version="1.0.0")

# Inclui as rotas
app.include_router(auth.router, tags=["Autenticação"])
app.include_router(student.router, tags=["Lista atividades de um aluno"])
app.include_router(activity.router, tags=["Detalhe da atividade"])
app.include_router(question.router, tags=["Lista questões / Detalhe da questão"])
