#!/usr/bin/python3
"""
The console module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNBCommand shell."""
    intro = 'Welcome to the HBNBCommand shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, inp):
        """Exit the command interpreter"""
        return True
    
    def do_EOF(self, line):
        "Exit the command interpreter"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
