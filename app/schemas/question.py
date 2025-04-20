from pydantic import BaseModel

class QuestionResponse(BaseModel):
    id: int
    text: str
    activity_id: int

    class Config:
        orm_mode = True
