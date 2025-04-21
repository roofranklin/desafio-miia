from pydantic import BaseModel
from typing import List, Optional, Literal


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

    class Config:
        orm_mode = True

