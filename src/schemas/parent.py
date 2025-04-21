from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from src.schemas.student import StudentCreate

class Parent(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str
    password: str
    inscription_date: datetime

class ParentCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    password: Optional[str] = None
    children: Optional[List[StudentCreate]] = None

class ParentResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str
    inscription_date: datetime
    children: List[StudentCreate]

    class Config:
        orm_mode = True