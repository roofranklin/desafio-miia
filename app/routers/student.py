from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, database

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=schemas.student.StudentOut)
def create_student(student: schemas.student.StudentCreate, db: Session = Depends(database.get_db)):
    db_student = db.query(models.student.Student).filter_by(email=student.email).first()
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_student = models.student.Student(email=student.email, password=student.password)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.get("/", response_model=List[schemas.student.StudentOut])
def list_students(db: Session = Depends(database.get_db)):
    return db.query(models.student.Student).all()
