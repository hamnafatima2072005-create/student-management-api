
from sqlalchemy.orm import Session
from .auth import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

from .database import get_db
from .schemas import StudentCreate
from . import crud
from fastapi import FastAPI, Depends, HTTPException
from .database import Base, engine, get_db
from . import models
from .schemas import (
    StudentCreate,
    StudentUpdate,
    UserCreate,
    UserResponse,
    UserLogin
)
from .auth import create_access_token, get_current_user
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Student Management API is running"
    }


@app.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return crud.create_student(db, student)


@app.get("/students")
def get_students(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return crud.get_students(db)

@app.get("/students/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student



@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    student = crud.update_student(
        db,
        student_id,
        student_data
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    student = crud.delete_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully",
        "student": student
    }

@app.post("/auth/signup", response_model=UserResponse)
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return crud.create_user(db, user)

@app.post("/auth/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    authenticated_user = crud.authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if authenticated_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token({
        "sub": str(authenticated_user.id)
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
 
@app.get("/profile")
def profile(
    current_user = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }