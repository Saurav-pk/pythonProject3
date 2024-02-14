from config.database import Base, engine
from sqlalchemy import Column, Integer, String


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String, index=True)
    department = Column(String, index=True)
    phone_number = Column(String, index=True)
    address = Column(String, index=True)


Base.metadata.create_all(bind=engine)
