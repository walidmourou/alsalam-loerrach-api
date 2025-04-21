from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class StudentBase(BaseModel):
    name: str
    birth_date: date
    level: str
    course: str
    prefered_time: str
    
class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    parent_id: int

    class Config:
        orm_mode = True

class Student(StudentBase):
    id: int
    parent_id: int

    class Config:
        orm_mode = True
