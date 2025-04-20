from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/activities")

@router.get("/{student_id}", response_model=list[schemas.ActivityResponse])
def get_activities(student_id: int, db: Session = Depends(get_db)):
    return db.query(models.Activity).filter(models.Activity.student_id == student_id).all()
