from fastapi import HTTPException
from fastapi import Depends
from fastapi import APIRouter

from sqlmodel import Session
from sqlmodel import select

from typing import Annotated

from db import get_session
from schemas import Car, CarInput
from schemas import Car_DBModel
from schemas import Trip, TripInput
from schemas import Trip_DBModel
from schemas import load_lib



router = APIRouter(prefix="/api/cars")


@router.post("/migrate", tags=['Generic'])
def migrate_data_to_db(session: Annotated[Session, Depends(get_session)]) -> list[Car_DBModel]:
    '''Currently, will duplicate if called multiple times.
    Trips data is not migrated as no data model for trips created yet.'''
    db = load_lib()
    lstCars = []
    for car in db:
        new_car = Car_DBModel.model_validate(car, update={'trips': []})
        session.add(new_car)
        session.commit()
        session.refresh(new_car)
        for trip in car.trips:
            new_trip = Trip_DBModel.model_validate(trip, update={'car_id': new_car.id, 'id': None})
            session.add(new_trip)
            session.commit()
            session.refresh(new_trip)
        lstCars.append(new_car)
    return lstCars


#region Car ################################################################################################################################
## Query Params     (http://localhost:8000?size=s&doors=4)
# Filter the data based on 'size' and/or 'doors'
@router.get("/", tags=['Car'])
def get_cars(session: Annotated[Session, Depends(get_session)], size:str|None=None, doors:int|None=None) -> list[Car]:
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
@router.get("/{id}", tags=['Car'])
def car_by_id(session: Annotated[Session, Depends(get_session)], id:int) -> Car:
    """Retrieve a specific ar by its id"""
    car = session.get(Car_DBModel, id)
    if car:
        return car
    else:
        return HTTPException(status_code=404, detail=f"No car with id={id}.")
        

## POST - To create an object on the server
@router.post("/", tags=['Car'])
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

@router.delete("/{id}", status_code=204, tags=['Car'])
def remove_car(session: Annotated[Session, Depends(get_session)], id: int):
    """Remove a car, specified by 'id',  from the server."""
    car = session.get(Car_DBModel, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id} found!")

@router.put("/{id}", response_model=Car_DBModel, tags=['Car'])
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

class BadTripException(Exception):  # Custom Exception Class
    pass


@router.post("/{car_id}/trips", tags=['Trips'])
def add_trip(session: Annotated[Session, Depends(get_session)], car_id: int, trip: TripInput) -> Trip_DBModel:
    car = session.get(Car_DBModel, car_id)
    if car:
        new_trip = Trip_DBModel.model_validate(trip, update={'car_id': car_id, 'id': None})
        if new_trip.start > new_trip.end:
            raise BadTripException("Trip end before start")
        car.trips.append(new_trip)
        session.commit()
        session.refresh(new_trip)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={car_id}")


@router.get("/{car_id}/trips", tags=['Trips'])
def get_trips(session: Annotated[Session, Depends(get_session)], car_id: int) -> list[Trip]:
    car = session.get(Car_DBModel, car_id)
    if car:
        car = Car.model_validate(car)
        if car.trips:
            return car.trips
        else:
            raise HTTPException(status_code=404, detail=f"No trips found for car with id={car_id}")
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={car_id} found!")

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

#endregion