#!/usr/bin/python3
"""This module contains the file storage class for the airBnB clone app"""
from json import dump, load, dumps, loads


class FileStorage:
    """This class is the storage engine for the airBnB clone app

    Attributes:
        __file_path (str): the path to the file where the objects are stored
        __objects (dict): the objects stored in the storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns all objects in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """This method adds a new object to storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """This method saves the objects in storage to a file"""
        with open(FileStorage.__file_path, "w") as file:
            obj_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            dump(obj_dict, file)

    def reload(self):
        """This method reloads the objects from the file to storage"""
        try:
            from models.base_model import BaseModel
            try:
                with open(FileStorage.__file_path, "r") as file:
                    obj_dict = load(file)
                    for key, obj in obj_dict.items():
                        cls_name = obj["__class__"]
                        cls_obj = eval(cls_name)(**obj)
                        FileStorage.__objects[key] = cls_obj
            except FileNotFoundError:
                pass
        except ImportError:
            pass
