from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Activity(Base):
    __tablename__ = "student"

    activity_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    id = Column(Integer, ForeignKey("students.id"))
    is_completed = Column(Boolean, default=False)

    student = relationship("Student", backref="student")
