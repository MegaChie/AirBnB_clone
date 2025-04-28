#!/usr/bin/python3
"""
Logic for the base model.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class for AirBnB clone project.

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Timestamp of instance creation.
        updated_at (datetime): Timestamp of last update to instance.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialises the class object
        """
        if kwargs:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a human-readable string representation of the object.
        """
        readable = "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

        return readable

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        dict = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key in ["updated_at", "created_at"]:
                value = value.isoformat()
            dict[key] = value

        return dict
