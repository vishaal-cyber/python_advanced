from fastapi import FastAPI

from contextlib import asynccontextmanager

from sqlmodel import SQLModel

from db import engine
from routers import cars
from routers import web



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


#endregion



############################################################################################################################################
if __name__ == "__main__":
    uvicorn.run("car_sharing:app")#, reload=True)
