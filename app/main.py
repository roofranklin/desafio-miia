from fastapi import FastAPI
from app.routers import activities

app = FastAPI()

app.include_router(activities.router)