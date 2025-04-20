from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/activity")

@router.get("/{id}", response_model=schemas.ActivityResponse)
def get_activity(id: int, db: Session = Depends(get_db)):
    activity = db.query(models.Activity).filter(models.Activity.id == id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")
    return activity

@router.patch("/{id}", response_model=schemas.ActivityResponse)
def update_activity(id: int, db: Session = Depends(get_db)):
    activity = db.query(models.Activity).filter(models.Activity.id == id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")
    activity.is_completed = False
    db.commit()
    db.refresh(activity)
    return activity

@router.post("/{id}", response_model=schemas.ActivityResponse)
def complete_activity(id: int, db: Session = Depends(get_db)):
    activity = db.query(models.Activity).filter(models.Activity.id == id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")
    activity.is_completed = True
    db.commit()
    db.refresh(activity)
    return activity
