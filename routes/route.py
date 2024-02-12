from fastapi import APIRouter
from models.student import Student
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_todos():
    students = list_serial(collection_name.find())
    return students

@router.post("/")
async def post_todo(student: Student):
    collection_name.insert_one(dict(student))
    return {"Success": "Item created!"}

@router.put("/{id}")
async def put_todo(id: str, student: Student):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(student)})
    return {"Success": "Item updated!"}

@router.delete(("/{id}"))
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"Success": "Item deleted!"}