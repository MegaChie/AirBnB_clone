#!/usr/bin/python3
"""
Command line interpreter for the project.
"""
import cmd
import re
import shlex
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
    objects = storage.all()

    def helper_class_check(self, class_name: Optional[str] = None,
                           ID: Optional[str] = None,
                           check_ID: bool = False) -> bool:
        """
        Checks the class and returns output as needed.
        """
        if not class_name and not ID:
            print("** class name missing **")
            return True

        if class_name not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return True

        if check_ID:
            if not ID:
                print("** instance id missing **")
                return True

        return False

    def helper_get_object(self, class_name: str, ID: str):
        """
        Returns an object based on it's class and ID.
        """
        key = f"{class_name}.{ID}"
        return HBNBCommand.objects.get(key)

    def helper_get_all(self, class_name: Optional[str] = None,
                       get_count: bool = False):
        objects_list = []
        if class_name and class_name in HBNBCommand.classes.keys():
            for key, value in HBNBCommand.objects.items():
                if key.startswith(class_name):
                    objects_list.append(str(value))

        else:
            for value in HBNBCommand.objects.values():
                objects_list.append(str(value))

        if get_count:
            return len(objects_list)

        return objects_list


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

    def emptyline(self) -> None:
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
            objects_list = self.helper_get_all()
            print(objects_list)
            return

        if self.helper_class_check(arg):
            return

        objects_list = self.helper_get_all(arg)
        print(objects_list)
        return

    def do_show(self, args) -> None:
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = shlex.split(args) or ["", ""]
        if len(args) == 1:
            args.append("")

        if self.helper_class_check(args[0], args[1], True):
            return

        object = self.helper_get_object(args[0], args[1])
        if object:
            print(object)
            return
        print("** no instance found **")
        return

    def do_destroy(self, args) -> None:
        """
        Deletes an instance based on the class name and id.
        """
        args = shlex.split(args) or ["", ""]
        if len(args) == 1:
            args.append("")
        if self.helper_class_check(args[0], args[1], True):
            return

        # Refactor
        object = self.helper_get_object(args[0], args[1])
        if object:
            key = f"{args[0]}.{args[1]}"
            del HBNBCommand.objects[key]
            storage.save()
            return
        print("** no instance found **")
        return

    def do_update(self, args) -> None:
        """
        Updates an instance based on the class name and id.
        """
        args = shlex.split(args) or ["", ""]
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
            object = self.helper_get_object(args[0], args[1])
            if not object:
                print("** no instance found **")
                return
            setattr(object, args[2], args[3])
            storage.save()
            return

    def default(self, line):
        """
        Handles advanced commands like <ClassName>.<command>()
        """
        simple_commands = {
            "all": self.do_all,
            "count": lambda one: print(self.helper_get_all(one,
                                                           get_count=True))
        }
        hard_commands = {
            "show": self.do_show,
            "destroy": self.do_destroy
        }
        command = re.match(r"^(\w+)\.(\w+)\((.*)\)$", line)
        if not command:
            print("*** Unknown syntax:", line)
            return

        class_name, command, intel = command.groups()
        if command in simple_commands.keys():
            simple_commands[command](class_name)
            return

        if command in hard_commands.keys():
            ID = intel.replace("\"", "").replace(",", "")
            hard_commands[command](f"{class_name} {intel}")
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
