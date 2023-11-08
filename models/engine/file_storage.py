#!/usr/bin/puython3
import json
from models.base_model import BaseModel
"""
serialization-deserialization of a JSON
"""


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        add new obj to existing instances
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        with open(FileStorage.__file_path, 'w') as file:
            json.dump({k: v.to_dict() for
                       k, v in FileStorage.__objects.items()}, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for k, v in data.items():
                    class_name, obj_id = k.split('.')
                    cls = eval(class_name)
                    obj = cls(**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
