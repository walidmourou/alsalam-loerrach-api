from pydantic import BaseModel
from typing import List

class Parent(BaseModel):
    id: int
    name: str
    email: str
    phone: str

class ParentCreate(BaseModel):
    name: str
    email: str
    phone: str

class ParentResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str

    class Config:
        orm_mode = True