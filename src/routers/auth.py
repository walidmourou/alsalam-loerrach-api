from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database.models import Parent
from ..database.connection import get_db
from ..schemas.parent import ParentCreate, ParentResponse
from ..auth.jwt_handler import create_jwt_token

router = APIRouter()

@router.post("/register", response_model=ParentResponse)
def register_parent(parent: ParentCreate, db: Session = Depends(get_db)):
    db_parent = db.query(Parent).filter(Parent.email == parent.email).first()
    if db_parent:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_parent = Parent(**parent.dict())
    db.add(new_parent)
    db.commit()
    db.refresh(new_parent)
    
    token = create_jwt_token(new_parent.id)
    return {"parent": new_parent, "token": token}

@router.post("/login", response_model=ParentResponse)
def login_parent(email: str, password: str, db: Session = Depends(get_db)):
    db_parent = db.query(Parent).filter(Parent.email == email).first()
    if not db_parent or not db_parent.verify_password(password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_jwt_token(db_parent.id)
    return {"parent": db_parent, "token": token}