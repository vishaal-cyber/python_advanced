from pydantic import BaseModel,ConfigDict,Field,constr,field_validator
# from typing import Optional
import re
import json
import os
from enum import Enum
import datetime as dt

class MemberStatus(str, Enum):
    available = "available"
    out_of_stock = "out_of_stock"
    discontinued = "discontinued"
    
class Member(BaseModel):
    id:int|None
    first_name:constr=Field(strip_whitespace=True,min_length=0,max_length=50,description="first Name of the member")
    last_name:constr=Field(strip_whitespace=True,min_length=0,max_length=50,description="last Name of the member")
    # models.EmailField(_(""), max_length=254)
    email:constr=Field(strip_whitespace=True)