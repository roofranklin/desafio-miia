from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/auth")

@router.post("", response_model=schemas.StudentResponse)
def authenticate(data: schemas.StudentAuth, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.email == data.email).first()
    if not student or student.password != data.password:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return student
