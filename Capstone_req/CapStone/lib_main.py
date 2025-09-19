from fastapi import FastAPI
import uvicorn
from fastapi import Request
# from sqlmodel import SQLModel
from http import HTTPStatus
import schema_books as schema_books

app=FastAPI(title="lib_Services")
print(schema_books.__file__)