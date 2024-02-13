#!/usr/bin/python3
"""
This task is the beginning of the cmd condole
where I was required to write a eof file,quit
and empty line method
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the main class that will be inheriring from the cmd module"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """This method is useful whenever we want to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """
        Used whan we want to quit the program, usage "<class quit>"
        """
        return True

    def emptyline(self):
        """Useful whenever a user preses enter without a command"""
        self.lastcmd = " "

    def do_create(self, line):
        """
        useful whenver we want to cerate a new instance of the base
        class model
        """
        new_base = BaseModel()
        if not line:
            print("** class name missing **")
        elif line is not "BaseModel":
            print("** class doesn't exist **")
        else:
            new_base.save()
            print(new_base.id())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
