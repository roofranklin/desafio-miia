from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/auth")

@router.post("", response_model=schemas.StudentResponse)
def authenticate(data: schemas.StudentAuth, db: Session = Depends(get_db)):
    """
    Autentica um estudante com base no email e senha.
    Args:
        data: O email e senha do estudante.
        db: A sessão do banco de dados.
    Raises:
        HTTPException: Se as credenciais forem inválidas.
    Returns:
        O estudante autenticado.
    """
    student = db.query(models.Student).filter(models.Student.email == data.email).first()
    if not student or student.password != data.password:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return student
