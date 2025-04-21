from pydantic import BaseModel
from typing import List, Optional

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    duration: int  # Duration in hours

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int

    class Config:
        orm_mode = True

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True

class CourseList(BaseModel):
    courses: List[Course]