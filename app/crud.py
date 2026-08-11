from sqlalchemy.orm import Session
from .schemas import StudentCreate, StudentUpdate, UserCreate, UserLogin
from .auth import hash_password, verify_password
from . import models



def create_student(db: Session, student: StudentCreate):
    new_student = models.Student(
        name=student.name,
        age=student.age,
        city=student.city
    )

    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

def get_students(db: Session):
    return db.query(models.Student).all()    

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

def update_student(
    db: Session,
    student_id: int,
    student_data: StudentUpdate
):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student is None:
        return None

    student.name = student_data.name
    student.age = student_data.age
    student.city = student_data.city

    db.commit()
    db.refresh(student)

    return student

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student is None:
        return None

    db.delete(student)
    db.commit()

    return student


def create_user(db: Session, user_data: UserCreate):
    hashed_password = hash_password(user_data.password)

    new_user = models.User(
        name=user_data.name,
        email=user_data.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
def authenticate_user(
    db: Session,
    email: str,
    password: str
):
    user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if user is None:
        return None

    if not verify_password(password, user.password):
        return None

    return user