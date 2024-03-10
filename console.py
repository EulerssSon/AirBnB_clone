#!/usr/bin/python3
"""This is the console module for the airBnB clone app
to run and test the app, run the console module
in active or interactive mode
"""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
