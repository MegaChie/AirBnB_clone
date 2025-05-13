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
    classes = {
                "BaseModel": "models.base_model",
                "User": "models.user",
                "City": "models.city",
                "State": "models.state",
                "Place": "models.place",
                "Review": "models.review",
                "Amenity": "models.amenity"
               }
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
                    if class_name in FileStorage.classes.keys():
                        module = __import__(FileStorage.classes[class_name],
                                            fromlist=[class_name])
                        cls = getattr(module, class_name)
                        FileStorage.__objects[key] = cls(**value)
        except Exception:
            pass
