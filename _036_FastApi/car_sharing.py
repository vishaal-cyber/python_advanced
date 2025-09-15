from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    """Returns a friendly welcome message."""
    return {'message': "Welcome to the Car Sharing Application"}


# Implement functionality for returning the current datetime
# return {'date': datetime.now()}
@app.get("/date")
def date():
    """Returns the date"""
    return {'date': datetime.now()}
