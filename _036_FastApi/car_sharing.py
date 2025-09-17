from datetime import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses  import FileResponse
from fastapi import Depends

from contextlib import asynccontextmanager

from sqlmodel import SQLModel
from sqlmodel import create_engine, Session
from sqlmodel import select

from typing import Annotated

# from typing import Optional
from schemas import Car, CarInput
from schemas import Car_DBModel
from schemas import Trip, TripInput
from schemas import load_lib, save_lib
import uvicorn

import os

#region Setup ################################################################################################################################
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


def get_session():
    with Session(engine) as session:
        yield session

#endregion

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


@app.post("/api/cars/migrate", tags=['Generic'])
def migrate_data_to_db() -> list[Car_DBModel]:
    '''Currently, will duplicate if called multiple times.
    Trips data is not migrated as no data model for trips created yet.'''
    db = load_lib()
    with Session(engine) as session:
        for car in db:
            new_car = Car_DBModel.model_validate(car)
            session.add(new_car)
        session.commit()
    return db

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#endregion

#region Car ################################################################################################################################
## Query Params     (http://localhost:8000/api/cars?size=s&doors=4)
# Filter the data based on 'size' and/or 'doors'
@app.get("/api/cars", tags=['Car'])
def get_cars(session: Annotated[Session, Depends(get_session)], size:str|None=None, doors:int|None=None) -> list[Car_DBModel]:
    """Returns a collection of cars from the server records."""
    query = select(Car_DBModel)
    if size:
        query = query.where(Car_DBModel.size == size)
    if doors:
        query = query.where(Car_DBModel.doors >= doors)

    result = session.exec(query).all()

    if result:
        return result  # of type Car_DBModel
    else:
        raise HTTPException(status_code=404, detail=f"No cars with size={size} and doors={doors}.")


## PATH Params
# Retrieve a specific car by id
@app.get("/api/cars/{id}", tags=['Car'])
def car_by_id(session: Annotated[Session, Depends(get_session)], id:int) -> Car_DBModel:
    """Retrieve a specific ar by its id"""
    car = session.get(Car_DBModel, id)
    if car:
        return car
    else:
        return HTTPException(status_code=404, detail=f"No car with id={id}.")
        

## POST - To create an object on the server
@app.post("/api/cars", tags=['Car'])
def add_car(session: Annotated[Session, Depends(get_session)], car: CarInput) -> Car_DBModel:
    """Add a new car to the collection"""
    # Need
    #   connectivity to db
    #   Session to operate in
    #   Operations (CRUD) 

    new_car = Car_DBModel.model_validate(car)
    session.add(new_car)
    print(f"{new_car = }")
    session.commit()
    print(f"{new_car = }")
    session.refresh(new_car)
    return new_car

@app.delete("/api/cars/{id}", status_code=204, tags=['Car'])
def remove_car(session: Annotated[Session, Depends(get_session)], id: int):
    """Remove a car, specified by 'id',  from the server."""
    car = session.get(Car_DBModel, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id} found!")

@app.put("/api/cars/{id}", response_model=Car_DBModel, tags=['Car'])
def change_car(session: Annotated[Session, Depends(get_session)], id: int, new_data: CarInput) -> Car_DBModel:
    """Replace a car, specified by 'id', on the server"""
    car = session.get(Car_DBModel, id)
    if car:
        car.fuel = new_data.fuel
        car.size = new_data.size
        car.doors = new_data.doors
        car.transmission = new_data.transmission
        session.commit()
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id} found!")

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

#endregion

#region Trips ##############################################################################################################################
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

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

#endregion

############################################################################################################################################
if __name__ == "__main__":
    uvicorn.run("car_sharing:app")#, reload=True)
