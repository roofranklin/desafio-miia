from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/question")

@router.get("/{id}", response_model=schemas.QuestionResponse)
def get_question(id: int, db: Session = Depends(get_db)):
    """
    Retorna uma questão por seu ID.
    Args:
        id (int): O ID da questão.
    Raises:
        HTTPException: Se a questão não for encontrada.
    Returns:
        QuestionResponse: A questão encontrada.
    """
    question = db.query(models.Question).filter(models.Question.id == id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Questão não encontrada")
    return question

@router.post("/{id}", response_model=schemas.AnswerResponse)
def submit_answer(id: int, data: schemas.AnswerCreate, db: Session = Depends(get_db)):
    """
    Submete uma resposta para uma questão específica pelo seu ID.
    Args:
        id (int): O ID da questão.
        data (AnswerCreate): Os dados da resposta a ser submetida.
        db (Session, optional): A sessão do banco de dados.
    Raises:
        HTTPException: Se a questão não for encontrada.
    Returns:
        AnswerResponse: A resposta submetida.
    """

    question = db.query(models.Question).filter(models.Question.id == id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Questão não encontrada")
    answer = models.Answer(**data.dict())
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer
