from fastapi import FastAPI
from fastapi import Request

from contextlib import asynccontextmanager

from sqlmodel import SQLModel

from db import engine
from routers import cars
from routers import web
from routers.cars import BadTripException

from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

# from typing import Optional
from db import engine
import uvicorn



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Code
    SQLModel.metadata.create_all(engine)

    # App 
    yield       # yield control to the 'app' object

    # Shutdown Code
    print("That's all folks!")


app = FastAPI(title="Car Sharing Services", lifespan=lifespan)
app.include_router(cars.router)
app.include_router(web.router)

@app.exception_handler(BadTripException)
async def uvicorn_exception_handler(request: Request, exc: BadTripException):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Bad trip"}
    )

@app.middleware("http")
async def add_cars_cookie(request: Request, call_next):
    response = await call_next(request)
    response.set_cookie(key="cars_cookie", value="you_visited_the_carsharing_app")
    return response

#endregion



############################################################################################################################################
if __name__ == "__main__":
    uvicorn.run("car_sharing:app")#, reload=True)
