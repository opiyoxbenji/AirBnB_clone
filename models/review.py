#!/usr/bin/python3
from models.base_model import BaseModel
"""
class review with inheritant attributes
"""


class Review(BaseModel):
    """
    inherates attributes from base_model
    """
    place_id = ""
    user_id = ""
    text = ""
