from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, database

router = APIRouter(prefix="/activities", tags=["Activities"])

@router.post("/", response_model=schemas.activity.ActivityOut)
def create_activity(activity: schemas.activity.ActivityCreate, student_id: int, db: Session = Depends(database.get_db)):
    student = db.query(models.student.Student).filter_by(id=student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    new_activity = models.activity.Activity(**activity.dict(), student_id=student_id)
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return new_activity

@router.get("/", response_model=List[schemas.activity.ActivityOut])
def list_activities(db: Session = Depends(database.get_db)):
    return db.query(models.activity.Activity).all()
