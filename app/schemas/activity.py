from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ActivityBase(BaseModel):
    name: str
    start_date: Optional[datetime] = None
    duration_minutes: int

class ActivityCreate(ActivityBase):
    pass

class ActivityOut(ActivityBase):
    id: int
    student_id: int
    class Config:
        orm_mode = True
