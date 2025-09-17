from datetime import datetime
from fastapi.responses  import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import Form, Depends
from fastapi import APIRouter

from sqlmodel import Session

from db import get_session
from routers.cars import get_cars

from starlette.responses import HTMLResponse

import os

router = APIRouter()

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "..", "templates"))


#region Generic #############################################################################################################################

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Returns a page to query for listing of cars in database, with options to filter on 'size' and 'doors'."""
    return templates.TemplateResponse("home.html",
                                      {"request": request})


@router.post("/search", response_class=HTMLResponse)
def search(*,
           size: str = Form(...), doors: int = Form(...),       # Form(...) --> no default value;  Form(2) --> default value of 2; type(...) --> class ellipsis
           request: Request, 
           session: Session = Depends(get_session)):
    cars = get_cars(size=size, doors=doors, session=session)    # No session injected by FastAPI, as it's a regular function call. So, we provide for it.
    return templates.TemplateResponse("search_results.html", 
                                      {"request": request, "cars": cars})

# Implement functionality for returning the current datetime
# return {'date': datetime.now()}
@router.get("/date", tags=['Generic'])
def date():
    """Returns the date"""
    return {'date': datetime.now()}

@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    """Serves the favicon.ico file"""
    return FileResponse(os.path.join(os.path.dirname(__file__), '..', 'static', 'sun.png'))


#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#endregion
