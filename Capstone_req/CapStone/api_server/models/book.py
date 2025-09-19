# from sqlmodel import SQLModel, Field,Relationship
from pydantic import BaseModel,ConfigDict,Field,constr,field_validator
# from typing import Optional
import re
import json
import os
from enum import Enum
import datetime as dt

class BookStatus(str, Enum):
    available = "available"
    out_of_stock = "out_of_stock"
    discontinued = "discontinued"
    
class library(BaseModel):
    id:str|None=Field(description="Unique identifier")
    title:constr = Field(None, strip_whitespace=True, min_length=0, max_length=0,description="Name of the book")
    author:constr=Field(None, strip_whitespace=True,min_length=0,max_length=100,description="Name of the author")
    isbn:str|None=None
    publication_year:int|None=Field(None,ge=1900,le=2025)
    genre:str|None=None
    total_copies:int=Field(None,ge=0)
    available_copies:int|None=None
    status:BookStatus|None=None
    created_at:dt.datetime|None=None#=Field#(default_factory=dt.UTC)
    updated_at:dt.datetime|None=None
    
    @field_validator("isbn")
    def validate_isbn(cls,v):
        if not re.match(r'/d',v):
            raise ValueError("invalid isbn number")
        return v
    
    
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
    