from datetime import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses  import FileResponse

from contextlib import asynccontextmanager

from sqlmodel import SQLModel
from sqlmodel import create_engine, Session
# from typing import Optional
from schemas import Car, CarInput
from schemas import Car_DBModel
from schemas import Trip, TripInput
from schemas import load_lib, save_lib
import uvicorn

import os

db = load_lib()


engine = create_engine(
    "sqlite:///carsharing.db", 
    connect_args={"check_same_thread": False},
    echo = True
)




@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Code
    SQLModel.metadata.create_all(engine)

    # App 
    yield       # yield control to the 'app' object

    # Shutdown Code
    print("That's all folks!")


app = FastAPI(title="Car Sharing Services", lifespan=lifespan)


#region Generic #############################################################################################################################

@app.get("/", tags=['Generic'])
def welcome():
    """Returns a friendly welcome message."""
    return {'message': "Welcome to the Car Sharing service"}


# Implement functionality for returning the current datetime
# return {'date': datetime.now()}
@app.get("/date", tags=['Generic'])
def date():
    """Returns the date"""
    return {'date': datetime.now()}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    """Serves the favicon.ico file"""
    return FileResponse(os.path.join(os.path.dirname(__file__), 'static', 'sun.png'))

#endregion


## Query Params     (http://localhost:8000/api/cars?size=s&doors=4)
# Filter the data based on 'size' and/or 'doors'
@app.get("/api/cars", tags=['Car'])
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
@app.get("/api/cars/{id}", tags=['Car'])
def car_by_id(id:int):
    """Retrieve a specific ar by its id"""
    # results = [car for car in db if car['id'] == id]
    results = [car for car in db if car.id == id]
    if results:
        return results[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}")


## POST - To create an object on the server
@app.post("/api/cars", tags=['Car']) #, response_model=Car)
def add_car(car: CarInput):
    """Add a new car to the collection"""
    # Need
    #   connectivity to db
    #   Session to operate in
    #   Operations (CRUD) 

    with Session(engine) as session:
        new_car = Car_DBModel.model_validate(car)
        session.add(new_car)
        print(f"{new_car = }")
        session.commit()
        print(f"{new_car = }")
        session.refresh(new_car)
    return new_car

@app.delete("/api/cars/{id}", status_code=204, tags=['Car'])
def remove_car(id: int):
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        db.remove(car)
        save_lib(db)
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id} found!")

@app.put("/api/cars/{id}", response_model=Car, tags=['Car'])
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
    
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

@app.post("/api/cars/{car_id}/trips", tags=['Trips'])
def add_trip(car_id: int, trip: TripInput) -> Trip:
    matches = [car for car in db if car.id == car_id]
    if matches:
        car = matches[0]
        new_trip = Trip(id=len(car.trips)+1,
                        start=trip.start,
                        end=trip.end,
                        description=trip.description)
        car.trips.append(new_trip)
        save_lib(db)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={car_id} found!")


@app.get("/api/cars/{car_id}/trips", tags=['Trips'])
def get_trips(car_id: int) -> list[Trip]:
    matches = [car for car in db if car.id == car_id]
    if matches:
        car = matches[0]
        if car.trips:
            return car.trips
        else:
            raise HTTPException(status_code=404, detail=f"No trips found for car with id={car_id}")
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={car_id} found!")




#####################################################################################################################
if __name__ == "__main__":
    uvicorn.run("car_sharing:app")#, reload=True)
