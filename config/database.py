from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:1234@cluster0.6d1yzmv.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]