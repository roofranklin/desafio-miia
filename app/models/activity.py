from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Interval
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    name = Column(String)
    start_date = Column(DateTime, default=datetime.utcnow)
    duration_minutes = Column(Integer)

    student = relationship("Student", back_populates="activities")
    questions = relationship("Question", back_populates="activity", cascade="all, delete-orphan")
