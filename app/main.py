from fastapi import FastAPI
from app.routers import activities

app = FastAPI()

app.include_router(activities.router)

# Criando tabelas automaticamente no banco de dados

from app.database import Base, engine
from app import models

Base.metadata.create_all(bind=engine)
