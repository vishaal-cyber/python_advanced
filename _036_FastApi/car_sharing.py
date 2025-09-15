from datetime import datetime
from fastapi import FastAPI
from fastapi.responses  import FileResponse

import os

db = [
    {"id": 1, "size": "s", f"fuel": "petrol",   "door": 3, "transmission": "auto"},
    {"id": 2, "size": "s", f"fuel": "electric", "door": 3, "transmission": "auto"},
    {"id": 3, "size": "s", f"fuel": "petrol",   "door": 5, "transmission": "manual"},
    {"id": 4, "size": "m", f"fuel": "electric", "door": 3, "transmission": "auto"},
    {"id": 5, "size": "m", f"fuel": "hybrid",   "door": 5, "transmission": "auto"},
    {"id": 6, "size": "m", f"fuel": "petrol",   "door": 4, "transmission": "manual"},
    {"id": 7, "size": "l", f"fuel": "disel",    "door": 4, "transmission": "manual"},
    {"id": 8, "size": "l", f"fuel": "petrol",   "door": 5, "transmission": "auto"},
    {"id": 9, "size": "l", f"fuel": "hybrid",   "door": 5, "transmission": "auto"}
]

app = FastAPI()

@app.get("/")
def welcome():
    """Returns a friendly welcome message."""
    return {'message': "Welcome to the Car Sharing service"}


# Implement functionality for returning the current datetime
# return {'date': datetime.now()}
@app.get("/date")
def date():
    """Returns the date"""
    return {'date': datetime.now()}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    """Serves the favicon.ico file"""
    return FileResponse(os.path.join(os.path.dirname(__file__), 'static', 'sun.png'))

# @app.get("/api/cars")
# def get_cars():
#     """Returns a collection of cars from the server records."""
#     return db


# Filter the data based on 'size'
@app.get("/api/cars")
def get_cars(size, doors:int):
    """Returns a collection of cars from the server records."""
    # if not isinstance(int(doors), int):
    #     raise TypeError("doors should be an integer")
    # # if size:
    #     return [car for car in db if car['size'] == size]
    # else:
    #     return db
    print(type(size), size, type(doors), doors)

    # return [car for car in db if car['size'] == size and car['door'] >= int(doors)]
    return [car for car in db if car['size'] == size and car['door'] >= doors]
