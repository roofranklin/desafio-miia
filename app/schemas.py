from pydantic import BaseModel
from datetime import datetime

class ActivityCreate(BaseModel):
    student_id: int
    start_time: datetime
    duration_minutes: int

class ActivityResponse(ActivityCreate):
    id: int

    class Config:
        orm_mode = True