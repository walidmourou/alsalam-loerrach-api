from sqlalchemy import Column, Integer, String, ForeignKey, Date, func, TIMESTAMP
from sqlalchemy.orm import relationship

from .connection import Base

class Parent(Base):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), unique=True, index=True)
    email = Column(String(320), unique=True, index=True)
    phone = Column(String(20), unique=True, index=True)
    address = Column(String(255))
    password = Column(String(255))
    inscription_date = Column(TIMESTAMP, default=func.now(), nullable=True)

    children = relationship("Student", back_populates="parent")

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), unique=True, index=True)
    birth_date = Column(Date)
    course = Column(String(50))
    level = Column(String(50))
    prefered_time = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parents.id'))

    parent = relationship("Parent", back_populates="children")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True)
    description = Column(String(1000))

    students = relationship("Student", secondary="course_students")

class CourseStudent(Base):
    __tablename__ = 'course_students'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)