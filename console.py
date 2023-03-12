#!/usr/bin/python3
""" Console """

import cmd
import json
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def update_dict(self, classname, uid, s_dict):
        """ Helper method for update() """
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_quit(self, line):
        """ exit the program """
        return True

    def do_EOF(self, line):
        """ exit the program """
        return True

    def emptyline(self):
        """ does nothing """
        pass

    def do_create(self, line):
        """ create class instance """
        argument = line.split(' ')
        if argument is None or argument[0] == "":
            print("** class name missing **")
        elif argument[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            newClass = storage.classes()[argument[0]]()
            newClass.save()
            print(newClass.id)

    def do_show(self, line):
        """  Prints the string representation of an instance """
        argument = line.split(' ')
        if argument is None or argument[0] == "":
            print("** class name missing **")
        else:
            if argument[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(argument) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(argument[0], argument[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """  Deletes an instance """
        argument = line.split(' ')
        if argument is None or argument[0] == "":
            print("** class name missing **")
        else:
            if argument[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(argument) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(argument[0], argument[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances """
        if line != "":
            argument = line.split(' ')
            if argument[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                text = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == argument[0]]
                print(text)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """ Counts the instances of a class """
        argument = line.split(' ')
        if not argument[0]:
            print("** class name missing **")
        elif argument[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """ Updates an instance by adding or updating attribute """
        if line == "" or line is None:
            print("** class name missing **")
            return
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
