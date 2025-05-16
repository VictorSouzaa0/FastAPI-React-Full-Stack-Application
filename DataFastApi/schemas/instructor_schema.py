from typing import Optional

from pydantic import BaseModel as SCBaseModel


class InstructorSchema(SCBaseModel):
    
    id: Optional[int] = None
    name: str
    age: int
    content: str
    image: str

    class Config:
        orm_mode = True