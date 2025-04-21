from pydantic import BaseModel
from typing import Optional, List, Literal
from datetime import datetime

class ObjectiveQuestion(BaseModel):
    item: str
    correct_answer: bool
    student_answer: Optional[bool] = None


class DiscursiveQuestion(BaseModel):
    item: str
    student_answer: Optional[str] = None
    grade: Optional[float] = None


class ComposeQuestion(BaseModel):
    student_answer: Optional[str] = None
    feedback: Optional[str] = None
    grade: Optional[float] = None


class QuestionResponse(BaseModel):
    id: str
    activity_id: int
    type: Literal["objective", "discursive", "compose"]
    title: str

    objective_items: Optional[List[ObjectiveQuestion]] = None
    discursive_items: Optional[List[DiscursiveQuestion]] = None
    compose: Optional[ComposeQuestion] = None

class ActivityBase(BaseModel):
    duration: int
    name: str
    description: Optional[str] = None
    questions: Optional[List[QuestionResponse]] = None

class ActivityUpdateResponse(BaseModel):
    id: int
    is_completed: bool

class ActivityCreate(ActivityBase):
    id: int

class ActivityCreateResponse(BaseModel):
    id: int
    is_completed: bool

class ActivityResponse(ActivityBase):
    id: int
    start_time: datetime
    is_completed: bool

class StudentProfile(BaseModel):
    id: int
    name: str
    email: str
    activities: Optional[List[ActivityResponse]] = None

    class Config:
        orm_mode = True
