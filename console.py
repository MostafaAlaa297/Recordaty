#!/usr/bin/python3

"""
Console
"""

import cmd
import models
from models.condition import Condition
from models.models import BaseModel
from models.reports import Report
from models.users import User
from models.visits import Visit
import shlex

classes = {"Condition": Condition, "BaseModel": BaseModel,
        "Report": Report, "User": User, "Visit": Visit}

class RecordatyCommand(cmd.Cmd):
    """ Recordaty Console """
    prompt = '(recordaty) '

    def do_EOF(self, arg):
        """Exit console"""
        return True

    def emptyline(self):
        """overwriting the emptyline method"""
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            pass # Logic required here
        else:
            print("** class doesn't exist **")
            return False

if __name__ == '__main__':
    RecordatyCommand().cmdloop()
