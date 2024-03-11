#!/usr/bin/python3
"""This is the console module for the airBnB clone app
to run and test the app, run the console module
in active or interactive mode
"""
import cmd
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json

my_classes = {
    "BaseModel": BaseModel, "User": User, "State": State, "City": City,
    "Place": Place, "Amenity": Amenity, "Review": Review
}


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
        if args not in my_classes:
            print("** class doesn't exist **")
            return
        new_instance = my_classes[args]()
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
        if args[0] not in my_classes:
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
        if args[0] not in my_classes:
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
        if args not in my_classes:
            print("** class doesn't exist **")
            return
        else:
            print([str(obj) for obj in models.storage.all().values()
                   if type(obj).__name__ == args])

    def do_update(self, args: str):
        """This method updates an instance

        Args:
            args (str):classid, attribute and value of the instance to update
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split(" ")
        if args[0] not in my_classes:
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

    def do_count(self, args: str) -> int:
        """This method counts the number of instances of a class

        Args:
            args (str): the class name of the instances to count
        Returns:
            int: the number of instances of the class
        """
        if not args or args == "":
            print(len(models.storage.all()))
            return
        if args not in my_classes:
            print("** class doesn't exist **")
            return
        else:
            print(len([obj for obj in models.storage.all().values()
                       if type(obj).__name__ == args]))

    def default(self, arg: str):
        """method handles the default behavior of the command interpreter"""
        if arg.find(".") != -1 and arg.find("(") != -1 and arg.find(")") != -1:
            if "count" in arg:
                arg = arg.replace("()", "")
                arg = arg.split(".")
                self.do_count(arg[0])
            elif "all" in arg:
                arg = arg.replace("()", "")
                arg = arg.split(".")
                self.do_all(arg[0])
            elif "show" in arg:
                ins_id = arg.find("(")
                ins_id = arg[ins_id + 2:arg.find(")") - 1]
                cls_name = arg[:arg.find(".")]
                if ins_id is None or len(ins_id.strip()) == 0:
                    self.do_show(cls_name)
                else:
                    self.do_show(f"{cls_name} {ins_id}")
            elif "destroy" in arg:
                ins_id = arg.find("(")
                ins_id = arg[ins_id + 2:arg.find(")") - 1]
                cls_name = arg[:arg.find(".")]
                # how to split a condtion in python on 2 lines
                # answer: use a backslash
                if ins_id.strip() == "None" or ins_id.strip()\
                        == "" or ins_id is None:
                    self.do_destroy(cls_name)
                else:
                    self.do_destroy(f"{cls_name} {ins_id}")
            elif "update" in arg:
                ins_id = arg.find("(")
                ins_id = arg[ins_id + 2:arg.find(",") - 1]
                cls_name = arg[:arg.find(".")]
                if cls_name not in my_classes:
                    print("** class doesn't exist **")
                    return
                if ins_id.strip() == "None" or ins_id.strip()\
                        == "" or ins_id is None:
                    print("** instance id missing **")
                    return
                if arg.find("{") != -1 and arg.find("}") != -1:
                    dict_str = arg[arg.find("{"):arg.find("}") + 1]
                    eval_dict = eval(dict_str)
                    key = f"{cls_name}.{ins_id}"
                    if key not in models.storage.all():
                        print("** no instance found **")
                        return
                    for k, v in eval_dict.items():
                        setattr(models.storage.all()[key], k, v)
                    models.storage.save()
                    return
                # how to count how many " in a string
                if arg.count('"') == 2:
                    print("** attribute name missing **")
                    return
                if arg.count('"') == 4:
                    print("** value missing **")
                    return
                arg = arg.split(", ")
                attr = arg[1].strip('"')
                value = arg[2].strip('"')
                value = arg[2].strip('")')
                self.do_update(f"{cls_name} {ins_id} {attr} {value}")
        else:
            return super().default(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
