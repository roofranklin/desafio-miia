from pydantic import BaseModel
from typing import Optional, List, Union
from enum import Enum

class QuestionType(str, Enum):
    objetiva = "objetiva"
    discursiva = "discursiva"
    redacao = "redacao"

# Estruturas para os dados específicos de cada tipo
class ObjetivaAlternativa(BaseModel):
    alternativa: str
    gabarito: bool
    resposta_aluno: Optional[bool] = None

class DiscursivaItem(BaseModel):
    item: str
    resposta_aluno: Optional[str] = None
    nota: Optional[float] = None

class RedacaoData(BaseModel):
    resposta_aluno: Optional[str] = None
    nota: Optional[float] = None

# Base para criação
class QuestionBase(BaseModel):
    type: QuestionType
    prompt: str
    objetiva_data: Optional[List[ObjetivaAlternativa]] = None
    discursiva_data: Optional[List[DiscursivaItem]] = None
    redacao_data: Optional[RedacaoData] = None

class QuestionCreate(QuestionBase):
    pass

class QuestionOut(QuestionBase):
    id: int
    activity_id: int
    class Config:
        orm_mode = True
