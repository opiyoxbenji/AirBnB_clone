#!/usr/bin/python3
"""
city class created
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from Basemodel"""
    state_id = ""
    name = ""
