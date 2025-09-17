from datetime import datetime
from fastapi.responses  import FileResponse
from fastapi import APIRouter
from starlette.responses import HTMLResponse

import os

router = APIRouter()


#region Generic #############################################################################################################################

@router.get("/", response_class=HTMLResponse)
def home():
    """Returns a welcome page."""
    return """
    <html>
        <head>
            <title>Car Sharing Demo</title>
        </head>
        <body>
            <h1>Welcome to the Car Sharing Service</h1>
            <p>Here is some text for you</p>
        </body>
    </html>
    """


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
