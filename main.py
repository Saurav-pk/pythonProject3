from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from auth.route import router, get_current_user, db_dependency
from config.database import SessionLocal
from models.student import Student

app = FastAPI()
app.include_router(router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class createStudentRequest(BaseModel):
    student_name: str
    department: str
    phone_number: str
    address: str


user_dependency = Annotated[dict, Depends(get_current_user)]


@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return {"User": user}


@app.post("/student")
async def post_create_student(user: user_dependency, student: createStudentRequest, db: Session = db_dependency):
    create_student_model = Student(
        student_name=student.student_name,
        department=student.department,
        phone_number=student.phone_number,
        address=student.address,  # Access password from student, not createStudentRequest
    )
    db.add(create_student_model)
    db.commit()
    return {"Success": "Item created!"}


@app.get("/getAll")
async def get_all_students(user: user_dependency, db: Session = db_dependency):
    students = db.query(Student).all()
    return students


@app.put("/{id}")
async def update_student(user: user_dependency, id: int, student: createStudentRequest, db: Session = db_dependency):
    existing_student = db.query(Student).filter(Student.id == id).first()
    if not existing_student:
        return {"error": "Student not found"}

    existing_student.student_name = student.student_name
    existing_student.department = student.department
    existing_student.phone_number = student.phone_number
    existing_student.address = student.address

    db.commit()
    return {"Success": "Item updated!"}


@app.delete("/{id}")
async def delete_student(user: user_dependency, id: int, db: Session = db_dependency):
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        return {"error": "Student not found"}

    db.delete(student)
    db.commit()
    return {"Success": "Item deleted!"}
