# class Car:
    # Initialiser
    # Properties 
    # __str__
    # __repr__

from pydantic import BaseModel
import json
import os

class CarInput(BaseModel):
    """Model for Car class"""
    # id: int
    size: str
    fuel: str|None = "electric"
    doors: int
    transmission: str|None = "auto"

class Car(CarInput):
    id: int


fileName = "cars.json"
filePath = os.path.join(os.path.dirname(__file__), fileName)

def load_lib() -> list[Car]:
    """Loads a list of Car data from a JSON file"""
    with open(filePath) as f:
        return [Car.model_validate(obj)  for obj in json.load(f)]

def save_lib(cars:list[Car]) -> None:
    """Stores a list of Car data to a JSON file"""
    with open(filePath, 'w') as f:
        json.dump([car.model_dump()   for car in cars], f, indent=4)        # car.model_dump() converts the Python-object to a Python-dictionary

