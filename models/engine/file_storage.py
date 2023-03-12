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

    def reload(self):
        """ Store first object """
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as opener:
            obj_dict = json.load(opener)
            obj_dict = {key: self.classes()[value["__class__"]](**v)
                        for key, value in obj_dict.items()}
            self.__objects = obj_dict

    def classes(self):
        from model.base_model import BaseModel
        from model.user import User
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes
