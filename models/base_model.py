"""This module contains the base model
the parent for all models in airBnB clone app"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """This class is the parent class for all models in the airBnB clone app"""

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        """This method initializes the base model

        Attributes:
            id (str): the unique id of the model
            created_at (datetime): the time the model was created
            updated_at (datetime): initially the same as created_at,
            but updated when the model is modified
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """This method returns the string representation of the model"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """This method updates the updated_at attribute to the current time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """This method returns a dictionary representation of the model"""
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict
