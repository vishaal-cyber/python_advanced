# from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from pydantic import ConfigDict
import json
import os

class TripInput(SQLModel):
    start: int
    end:int
    description: str

class Trip(TripInput):
    id: int

class CarInput(SQLModel):
    """Model for Car class"""
    # id: int
    size: str
    fuel: str|None = "electric"
    doors: int
    transmission: str|None = "auto"

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "size": "cfg-size",
                "fuel": "tesla",
                "doors": 4,
                "transmission": "automatic"
            }
        }
    )


class Car_DBModel(CarInput, table=True):
    id: int|None = Field(primary_key=True, default=None)
    

class Car(CarInput):
    id: int
    trips: list[Trip] = []



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

