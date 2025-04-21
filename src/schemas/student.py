from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    age: int
    email: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int

    class Config:
        orm_mode = True

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class StudentList(BaseModel):
    students: List[Student]