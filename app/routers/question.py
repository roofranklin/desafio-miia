from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/question")

@router.get("/{id}", response_model=schemas.QuestionResponse)
def get_question(id: int, db: Session = Depends(get_db)):
    question = db.query(models.Question).filter(models.Question.id == id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Questão não encontrada")
    return question

@router.post("/{id}", response_model=schemas.AnswerResponse)
def submit_answer(id: int, data: schemas.AnswerCreate, db: Session = Depends(get_db)):
    question = db.query(models.Question).filter(models.Question.id == id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Questão não encontrada")
    answer = models.Answer(**data.dict())
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer
