from datetime import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses  import FileResponse
# from typing import Optional
from schemas import Car
from schemas import load_lib
import uvicorn

import os

db = load_lib()

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


## Query Params     (http://localhost:8000/api/cars?size=s&doors=4)
# Filter the data based on 'size' and/or 'doors'
@app.get("/api/cars")
def get_cars(size:str|None=None, doors:int|None=None) -> list[Car]:
    """Returns a collection of cars from the server records."""
    results = db

    if size:
        results =  [car for car in results if car.size == size]

    if doors:
        results =  [car for car in results if car.doors >= doors]

    return results


## PATH Params
# Retrieve a specific car by id
@app.get("/api/cars/{id}")
def car_by_id(id:int):
    """Retrieve a specific ar by its id"""
    # results = [car for car in db if car['id'] == id]
    results = [car for car in db if car.id == id]
    if results:
        return Car.model_validate(results[0])
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}")

if __name__ == "__main__":
    uvicorn.run("car_sharing:app")#, reload=True)