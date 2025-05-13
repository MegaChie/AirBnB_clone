#!/usr/bin/python3
"""
Logic for the storage model.
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        to_write = {}
        for key, value in FileStorage.__objects.items():
            to_write[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as cursor:
            json.dump(to_write, cursor)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, "r") as cursor:
                objects = json.load(cursor)
                for key, value in objects.items():
                    class_name = value["__class__"]
                    module = __import__("models.base_model" and "models.user"
                                        and "models.city" and "models.state"
                                        and "models.place" and "models.review"
                                        and "models.amenity",
                                        fromlist=[class_name])
                    cls = getattr(module, class_name)
                    FileStorage.__objects[key] = cls(**value)
        except Exception:
            pass
