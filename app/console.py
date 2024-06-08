#!/usr/bin/python3

"""
Console
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

import cmd
import re
import models
from models.users import User
from models.condition import Condition
from models.models import BaseModel
from models.reports import Report
from models.visits import Visit

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
        """Creates a new instance of the specified class"""
        args = arg.split()
        instance_dict = {}
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[args[0]]()
            for argument in args[1:]:
                splitted = argument.split("=")
                if len(splitted) == 2:
                    key = splitted[0]
                    val = splitted[1]
                    print(key)
                    print(val)
                    if val.startswith('"') and val.endswith('"'):
                        val_spaced = val.replace("_", " ")
                        val_final = val_spaced.replace("\"", "")
                        print(val_spaced + " Spaced value " + val)
                        setattr(new_instance, key, val_final)
                        print('1')
                    elif re.search("^-?\d+\.{1}\d+$", val):
                        val = float(val)
                        print("float is " + str(val))
                        setattr(new_instance, key, val)
                        print('2')
                    elif re.search("^-?\d+$", val):
                        val = int(val)
                        setattr(new_instance, key, val)
                        print("int is " + str(val))
                        print('3')
                else:
                    pass
                
            new_instance.save()
            print(new_instance.id)

if __name__ == '__main__':
    RecordatyCommand().cmdloop()
