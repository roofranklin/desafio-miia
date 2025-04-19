from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, database

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.post("/", response_model=schemas.question.QuestionOut)
def create_question(question: schemas.question.QuestionCreate, activity_id: int, db: Session = Depends(database.get_db)):
    activity = db.query(models.activity.Activity).filter_by(id=activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    new_question = models.question.Question(**question.dict(), activity_id=activity_id)
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

@router.get("/", response_model=List[schemas.question.QuestionOut])
def list_questions(db: Session = Depends(database.get_db)):
    return db.query(models.question.Question).all()
