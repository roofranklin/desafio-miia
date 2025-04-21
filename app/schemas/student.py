from pydantic import BaseModel

class StudentAuth(BaseModel):
    email: str
    password: str

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    authenticated: bool

    class Config:
        orm_mode = True
