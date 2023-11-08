#!/usr/bin/python3
import uuid
from datetime import datetime

"""
Base Model
Defines all common attributes and methods for other classes
"""


class BaseModel:
    """
    base class with attributes for other classes
    """
    def __init__(self):
        """
        initialize attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)