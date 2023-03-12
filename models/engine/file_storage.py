#!/usr/bin/python3
""" FileStorage """


import json
import datetime
import os


class FileStorage:
    """ Store first object """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Store first object """
        return self.__objects

    def new(self, obj):
        """ Store first object """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Store first object """
        with open(self.__file_path, "w", encoding="utf-8") as writer:
            d = {key: value.to_dict() for
                 key, value in self.__objects.items()}
            json.dump(d, writer)

    def classes(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """ Store first object """
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as opener:
            objDict = json.load(opener)
            objDict = {k: self.classes()[v["__class__"]](**v)
                       for k, v in objDict.items()}
            self.__objects = objDict
