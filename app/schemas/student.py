from typing import List, Optional
from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    email: EmailStr

class StudentCreate(StudentBase):
    password: str

class StudentOut(StudentBase):
    id: int
    class Config:
        orm_mode = True
