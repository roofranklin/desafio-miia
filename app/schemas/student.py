from pydantic import BaseModel

class StudentAuth(BaseModel):
    email: str
    password: str

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
