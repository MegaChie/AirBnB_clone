#!/usr/bin/python3
"""
Command line interpreter for the project.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class object for the interpreter.
    """
    prompt = "(hbnb) "
    classes = {
               "BaseModel": BaseModel(), "User": User()
               }

    def do_quit(self, arg):
        """
        Terminates the interpreter.
        """
        exit()

    def do_EOF(self, arg):
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

    def do_create(self, arg):
        """
        Creates a new instance of a model object, saves it then prints its ID.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        else:
            new_object = HBNBCommand.classes[arg]
            new_object.save()
            object_dict = new_object.to_dict()
            print(object_dict["id"])
            return

    def do_all(self, arg):
        if not arg:
            objects = storage.all()
            objects_list = []
            for object in objects.values():
                objects_list.append(str(object))
            print(objects_list)
            return
        elif arg not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        else:
            objects = storage.all()
            objects_list = []
            for key, value in objects.items():
                if arg in key:
                    objects_list.append(str(value))
            print(objects_list)
            return

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            objects = storage.all()
            for key, value in objects.items():
                temp = key.split(".")
                if temp[1] == args[1]:
                    print(str(value))
                    return
            print("** no instance found **")
            return

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            objects = storage.all()
            for object in objects:
                temp = object.split(".")
                if temp[1] == args[1]:
                    del objects[object]
                    storage.save()
                    return
            print("** no instance found **")
            return

    def do_update(self,args):
        """
        Updates an instance based on the class name and id.
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
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
                if temp[1] == args[1]:
                    setattr(value, attribute[0], attribute[1])
                    storage.save()
                    return
            print("** no instance found **")
            return



if __name__ == "__main__":
    HBNBCommand().cmdloop()
