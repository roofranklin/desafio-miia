from fastapi import FastAPI
from app.database import Base, engine
from app.routers import student, activity, question

# Cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MIIA API")

# Inclui as rotas
app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(activity.router, prefix="/activities", tags=["Activities"])
app.include_router(question.router, prefix="/questions", tags=["Questions"])
