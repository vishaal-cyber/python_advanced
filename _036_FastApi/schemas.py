# class Car:
    # Initialiser
    # Properties 
    # __str__
    # __repr__

from pydantic import BaseModel
import json
import os

class Car(BaseModel):
    """Model for Car class"""
    id: int
    size: str
    fuel: str|None = "electric"
    doors: int
    transmission: str|None = "auto"

fileName = "cars.json"
filePath = os.path.join(os.path.dirname(__file__), fileName)

def load_lib():
    """Loads a list of Car data from a JSON file"""
    with open(filePath) as f:
        return [Car.model_validate(obj)  for obj in json.load(f)]
