from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..schemas.student import StudentCreate, StudentResponse
from ..database.models import Student

router = APIRouter()

@router.post("/students/", response_model=StudentResponse)
def register_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student