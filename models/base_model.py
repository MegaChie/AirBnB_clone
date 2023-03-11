#!/usr/bin/python3
""" BaseModel """


import uuid
from datetime import datetime
# from models import storage


class BaseModel:
    """ BaseModel """
    def __init__(self, *args, **kwargs):
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)

    def __str__(self):
        """ BaseModel """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ BaseModel """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ BaseModel """
        newDict = self.__dict__.copy()
        newDict["__class__"] = type(self).__name__
        newDict["created_at"] = newDict["created_at"].isoformat()
        newDict["updated_at"] = newDict["updated_at"].isoformat()
        return newDict
