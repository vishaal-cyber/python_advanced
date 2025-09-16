from datetime import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses  import FileResponse
# from typing import Optional
from schemas import Car, CarInput
from schemas import load_lib, save_lib
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

    if results:
        return results
    else:
        raise HTTPException(status_code=404, detail=f"No cars with size={size} and doors={doors}.")


## PATH Params
# Retrieve a specific car by id
@app.get("/api/cars/{id}")
def car_by_id(id:int):
    """Retrieve a specific ar by its id"""
    # results = [car for car in db if car['id'] == id]
    results = [car for car in db if car.id == id]
    if results:
        return results[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}")


## POST - To create an object on the server
@app.post("/api/cars") #, response_model=Car)
def add_car(car: CarInput) -> Car:
    """Add a new car to the collection"""
    id = len(db) + 1
    new_car = Car(id=id, size=car.size, fuel=car.fuel, doors=car.doors, transmission=car.transmission)
    db.append(new_car)
    save_lib(db)
    # new_car =  [obj for obj in db if obj.id == car.id]
    return new_car
    # return str(new_car)
    # return "Done"

@app.delete("/api/cars/{id}", status_code=204)
def remove_car(id: int):
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        db.remove(car)
        save_lib(db)
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id} found!")

@app.put("/api/cars/{id}", response_model=Car)
def change_car(id: int, new_data: CarInput) -> Car:
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        car.fuel = new_data.fuel
        car.size = new_data.size
        car.doors = new_data.doors
        car.transmission = new_data.transmission
        save_lib(db)
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id} found!")
    
if __name__ == "__main__":
    uvicorn.run("car_sharing:app")#, reload=True)
