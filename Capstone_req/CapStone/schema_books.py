# from sqlmodel import SQLModel, Field,Relationship
from pydantic import BaseModel,ConfigDict
import json
import os

class library(BaseModel):
    id:str|None=None
    title:str|None=None
    author:str|None=None
    isbn:str|None=None
    publication_year:int|None=None
    genre:str|None=None
    total_copies:int|None=None
    available_copies:int|None=None
    status:str|None=None
    created_at:str|None=None
    updated_at:str|None=None
    
    model_config=ConfigDict(
        json_schema_extra={
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "isbn": "9780743273565",
            "publication_year": 1925,
            "genre": "Fiction",
            "total_copies": 5,
            "available_copies": 3,
            "status": "available",
            "created_at": "2024-01-01T10:00:00",
            "updated_at": "2024-01-01T10:00:00"
        }
    )

fileName="books.json"
print(os.path.dirname(__file__))
filepath=os.path.join(os.path.dirname(__file__),"/data",fileName)
print(filepath)



def load_data() -> list[library]:
    "loads the data from books.json"
    with open(filepath) as f:
        return [library.model_validate(obj) for obj in json.load(f)]
    
def save_date() -> list[library]:
    "save data to the books.json"
    with open(filepath,"w") as f:
        json.dump([lib.model_dump() for lib in library],f,indent=4)
# class Libinput(SQLModel):
#     id:int
    