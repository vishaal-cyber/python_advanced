# class Car:
    # Initialiser
    # Properties 
    # __str__
    # __repr__

from pydantic import BaseModel

class Car(BaseModel):
    id: int
    size: str
    fuel: str|None = "electric"
    doors: int
    transmission: str|None = "auto"
