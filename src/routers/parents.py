from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..schemas.parent import ParentCreate, ParentResponse
from ..database.models import Parent

router = APIRouter()

@router.post("/parents/", response_model=ParentResponse)
def register_parent(parent: ParentCreate, db: Session = Depends(get_db)):
    db_parent = Parent(**parent.dict())
    db.add(db_parent)
    db.commit()
    db.refresh(db_parent)
    return db_parent

@router.get("/parents/{parent_id}", response_model=ParentResponse)
def get_parent(parent_id: int, db: Session = Depends(get_db)):
    db_parent = db.query(Parent).filter(Parent.id == parent_id).first()
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return db_parent