#!/usr/bin/python3
"""
Command line interpreter for the project.
"""
import cmd
from typing import Optional
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Class object for the interpreter.
    """
    prompt = "(hbnb) "
    classes = {
               "Amenity": Amenity, "BaseModel": BaseModel,
               "City": City, "Place": Place,
               "Review": Review, "State": State,
               "User": User
               }

    def helper_class_check(self, name: Optional[str] = None,
                           ID: Optional[str] = None,
                           check_ID: bool = False) -> bool:
        """
        Checks the class and returns output as needed.
        """
        if not name and not ID:
            print("** class name missing **")
            return True

        if name not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return True

        if check_ID:
            if not ID:
                print("** instance id missing **")
                return True

        return False


    def do_quit(self, arg: str) -> None:
        """
        Terminates the interpreter.
        """
        exit()

    def do_EOF(self, arg: str) -> Optional[bool]:
        """
        Handles the EOF signal to exit the interpreter.
        """
        print()
        return True

    def emptyline(self):
        """
        Overrides the default behavior of repeating the last command
        when an empty line is entered.
        """
        pass

    def do_create(self, arg: str) -> None:
        """
        Creates a new instance of a model object, saves it then prints its ID.
        """
        if self.helper_class_check(arg):
            return

        new_object = HBNBCommand.classes[arg]()
        new_object.save()
        object_dict = new_object.to_dict()
        print(object_dict["id"])
        return

    def do_all(self, arg: str) -> None:
        if not arg:
            objects = storage.all()
            objects_list = []
            for object in objects.values():
                objects_list.append(str(object))
            print(objects_list)
            return

        if self.helper_class_check(arg):
            return

        objects = storage.all()
        objects_list = []
        for key, value in objects.items():
            if arg in key:
                objects_list.append(str(value))
        print(objects_list)
        return

    def do_show(self, args) -> None:
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = args.split()
        if len(args) == 1:
            args.append("")

        if self.helper_class_check(args[0], args[1], True):
            return

        objects = storage.all()
        for key, value in objects.items():
            temp = key.split(".")
            if temp[0] == args[0] and temp[1] == args[1]:
                print(str(value))
                return
        print("** no instance found **")
        return

    def do_destroy(self, args) -> None:
        """
        Deletes an instance based on the class name and id.
        """
        args = args.split() or ["", ""]
        if len(args) == 1:
            args.append("")
        if self.helper_class_check(args[0], args[1], True):
            return

        objects = storage.all()
        for object in objects:
            temp = object.split(".")
            if temp[0] == args[0] and temp[1] == args[1]:
                del objects[object]
                storage.save()
                return
        print("** no instance found **")
        return

    def do_update(self,args) -> None:
        """
        Updates an instance based on the class name and id.
        """
        args = args.split()
        if len(args) == 1:
            args.append("")
        if self.helper_class_check(args[0], args[1], True):
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            objects = storage.all()
            attribute = args[2::]
            attribute[1] = attribute[1].strip("\"")
            objects = storage.all()
            for key, value in objects.items():
                temp = key.split(".")
                if temp[0] == args[0] and temp[1] == args[1]:
                    setattr(value, attribute[0], attribute[1])
                    storage.save()
                    return
            print("** no instance found **")
            return

    def default(self, line):
        """
        Handels advantage commands that are like <ClassName>.<command>
        """
        command = line.split(".")
        try:
            if command[1] == "all()":
                if command[0] in HBNBCommand.classes.keys():
                    objects = storage.all()
                    class_objects = []
                    for key, value in objects.items():
                        temp = key.split(".")
                        if temp[0] == command[0]:
                            class_objects.append(str(value))
                    print("[{}]".format(", ".join(class_objects)))
                    return
                else:
                    print("** class doesn't exist **")
                    return
        except IndexError:
            print("*** Unknown syntax: {} ***".format(line))
            return

    def do_exeAll(self, arg):
        self.do_all(arg)



if __name__ == "__main__":
    HBNBCommand().cmdloop()
