from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/student")

@router.get("/{id}", response_model=schemas.StudentProfile)
def get_student(student_id: int, db: Session = Depends(get_db)):
    return db.query(models.Activity).filter(models.Activity.student_id == student_id).all()
