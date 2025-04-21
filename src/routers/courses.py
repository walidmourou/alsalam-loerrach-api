from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import models
from ..database.connection import get_db
from ..schemas.course import CourseCreate, CourseResponse
from ..auth.jwt_bearer import JwtBearer

router = APIRouter()

@router.post("/courses/", response_model=CourseResponse, dependencies=[Depends(JwtBearer())])
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/courses/{course_id}", response_model=CourseResponse, dependencies=[Depends(JwtBearer())])
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.get("/courses/", response_model=list[CourseResponse], dependencies=[Depends(JwtBearer())])
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(models.Course).all()
    return courses