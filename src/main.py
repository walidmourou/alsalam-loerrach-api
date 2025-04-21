from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, courses, students, parents
from .database.connection import init_db

app = FastAPI()

# Initialize database
@app.on_event("startup")
async def startup_event():
    init_db()

# CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://alsalam-loerrach.org"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(students.router)
app.include_router(parents.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}