#!/usr/bin/python3
"""This is the console module for the airBnB clone app
to run and test the app, run the console module
in active or interactive mode
"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import models
import json

classes = {"BaseModel": BaseModel, "User": User}


class HBNBCommand(cmd.Cmd):
    """This class is the command interpreter for the airBnB clone app
    Attributes:
        prompt (str): the prompt for the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self) -> bool:
        """This method does nothing when the user hits enter"""
        return False

    def do_create(self, args):
        """This method creates a new instance of a model

        Args:
            args (str): the class name of the model to create
        Returns:
            None
        """
        if not args or args == "":
            print("** class name missing **")
            return
        if args not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """This method prints the string representation of an instance

        Args:
            args (str): the class name and id of the instance to show
        Returns:
            None
        """
        if not args or args == "":
            print("** class name missing **")
            return
        args = args.split(" ")
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, args):
        """This method deletes an instance

        Args:
            args (str): the class name and id of the instance to delete
        Returns:
            None
        """
        if not args or args == "":
            print("** class name missing **")
            return
        args = args.split(" ")
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        # del not pop to make sure never trust garbage collector
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, args):
        """This method prints the string representation of all instances

        Args:
            args (str): the class name of the instances to show
        """
        if not args or args == "":
            print([str(obj) for obj in models.storage.all().values()])
            return
        if args not in classes:
            print("** class doesn't exist **")
            return
        else:
            print([str(obj) for obj in models.storage.all().values()
                   if type(obj).__name__ == args])

    def do_update(self, args: str):
        """This method updates an instance

        Args:
            args (str): the class name, id, attribute
            and value of the instance to update
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split(" ")
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        # cast the value to the type of the attribute
        attr = args[2]
        value = args[3]
        if value.isdigit():
            value = int(value)
        elif '.' in value and value.replace('.', '').isdigit():
            value = float(value)
        else:
            value = str(value)
        setattr(models.storage.all()[key], attr, value)
        models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
