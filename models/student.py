from pydantic import BaseModel

class Student(BaseModel):
    student_name: str
    student_id: str
    department: str
    phone_number: str
    address: str