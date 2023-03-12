#!/usr/bin/python3
""" Console """

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ exit the program """
        return True

    def do_EOF(self, line):
        """ exit the program """
        return True

    def emptyline(self):
        """ does nothing """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
