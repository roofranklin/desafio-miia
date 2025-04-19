from sqlalchemy import Column, Integer, String, ForeignKey, Text, Enum, Float, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class QuestionType(str, enum.Enum):
    objetiva = "objetiva"
    discursiva = "discursiva"
    redacao = "redacao"

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"))
    type = Column(Enum(QuestionType))
    prompt = Column(Text)

    # Armazena os dados específicos de cada tipo de questão
    objetiva_data = Column(JSONB, nullable=True)  # Lista de alternativas
    discursiva_data = Column(JSONB, nullable=True)  # Lista de itens
    redacao_data = Column(JSONB, nullable=True)  # Texto e nota

    activity = relationship("Activity", back_populates="questions")
