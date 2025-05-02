#!/usr/bin/python3
"""
Command line interpreter for the project.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class object for the interpreter.
    """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
