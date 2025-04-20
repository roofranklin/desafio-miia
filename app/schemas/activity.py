from pydantic import BaseModel
from typing import Optional

class ActivityBase(BaseModel):
    title: str
    description: Optional[str] = None

class ActivityCreate(ActivityBase):
    student_id: int

class ActivityResponse(ActivityBase):
    id: int
    is_completed: bool

    class Config:
        orm_mode = True
