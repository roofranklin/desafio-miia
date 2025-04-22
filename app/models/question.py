from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class ObjectiveQuestion(Base):
    __tablename__ = "objective_questions"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, nullable=False)
    correct_answer = Column(Boolean, nullable=False)
    student_answer = Column(Boolean, nullable=True)

class DiscursiveQuestion(Base):
    __tablename__ = "discursive_questions"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, nullable=False)
    student_answer = Column(String, nullable=True)
    grade = Column(Float, nullable=True)

class ComposeQuestion(Base):
    __tablename__ = "compose_questions"

    id = Column(Integer, primary_key=True, index=True)
    student_answer = Column(String, nullable=True)
    feedback = Column(String, nullable=True)
    grade = Column(Float, nullable=True)

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    activity_id = Column(Integer, ForeignKey("student.id"))
    
    objective_items = relationship("ObjectiveQuestion", backref="question")
    discursive_items = relationship("DiscursiveQuestion", backref="question")
    compose = relationship("ComposeQuestion", backref="question")
    activity = relationship("Activity", backref="questions")
