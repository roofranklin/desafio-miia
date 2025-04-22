from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/activity")

@router.get("/{id}", response_model=schemas.ActivityResponse)
def get_activity(id: int, db: Session = Depends(get_db)):
    """
    Retorna uma atividade específica pelo seu ID.
    Args:
        id (int): O ID da atividade.
    Raises:
        HTTPException: Se a atividade não for encontrada.
    Returns:
        ActivityResponse: A atividade encontrada.
    """
    activity = db.query(models.Activity).filter(models.Activity.id == id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")
    return activity

@router.patch("/{id}", response_model=schemas.ActivityUpdateResponse)
def update_activity(data: schemas.ActivityBase, db: Session = Depends(get_db)):
    """
    Quando um aluno salva uma atividade em andamento, atualiza uma atividade específica pelo seu ID.
    Args:
        data (ActivityBase): Os dados da atividade a ser atualizada.
    Raises:
        HTTPException: Se a atividade não for encontrada.
    Returns:
        ActivityUpdateResponse: A atividade atualizada.
    """
    activity = db.query(models.Activity).filter(models.Activity.id == data.id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")
    activity.is_completed = False
    db.commit()
    db.refresh(activity)
    return activity

@router.post("/{id}", response_model=schemas.ActivityCreateResponse)
def complete_activity(data: schemas.ActivityBase, db: Session = Depends(get_db)):
    """
    Quando o aluno clica em concluir, completa uma atividade específica pelo seu ID.
    Args:
        data (ActivityBase): Os dados da atividade a ser completada.
    Raises:
        HTTPException: Se a atividade não for encontrada.
    Returns:
        ActivityCreateResponse: A atividade completada.
    """
    activity = db.query(models.Activity).filter(models.Activity.id == data.id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")
    activity.is_completed = True
    db.commit()
    db.refresh(activity)
    return activity
