from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    answer_text = Column(String)

    question = relationship("Question", backref="answers")
    student = relationship("Student", backref="answers")
