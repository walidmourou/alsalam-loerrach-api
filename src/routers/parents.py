from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..schemas.parent import ParentCreate, ParentResponse
from ..database.models import Parent, Student
from src.utils import generate_random_string

router = APIRouter()

@router.post("/parents/", response_model=ParentResponse)
def register_parent(parent: ParentCreate, db: Session = Depends(get_db)):
    # Generate random password if not provided
    if not parent.password:
        parent.password = generate_random_string(10)
    
    # Extract children data and remove it from parent dict
    parent_data = parent.model_dump()
    children_data = parent_data.pop('children', None)
    
    # Create parent instance
    db_parent = Parent(**parent_data)
    db.add(db_parent)
    db.flush()  # Flush to get the parent ID
    
    # Create children if provided
    if children_data:
        for child_data in children_data:
            db_student = Student(**child_data, parent_id=db_parent.id)
            db.add(db_student)
    
    db.commit()
    db.refresh(db_parent)
    return db_parent

@router.get("/parents/{parent_id}", response_model=ParentResponse)
def get_parent(parent_id: int, db: Session = Depends(get_db)):
    db_parent = db.query(Parent).filter(Parent.id == parent_id).first()
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return db_parent