This project is the start of my journey to develop a full web App the Airbnb Clone. Its suposed to work exactly as thr main Airbnb website. In rhis section of the project I will be creating the backend parr of the Airbnb project. For this I'll be using Python, while for the Front End I'll use Cmd for the momment because, I'm yet to reach the web development section in my leaening. 

The cmd module in Python is a tool for creating simple command-line interfaces. It's particularly useful when you want to build an interactive program where users can input commands and get responses. The cmd module helps one create a custom command prompt where users can type commands and interact with your program. 

For one to use it he/she has to define a class that inherits from cmd.Cmd.
Inside this class, one defines methods that start with "do_" for each command you want to support.

The cmd.Cmd class handles user input, command dispatching, and error handling for you.
Each method one defines in his/her class that starts with "do_" represents a command.
These methods typically take two arguments: self (the instance of your class) and line (the string entered by the user after the command name).

One can implement the logic for each command inside its corresponding method.
You can customize the command prompt by setting the prompt attribute in your class.

You can start the command loop by calling the cmdloop() method on an instance of your class.

lastly in order to exit the program , you define a command method (e.g., do_quit) to exit the program gracefully.

an example of this concept is as follows:

import cmd

class MyCmd(cmd.Cmd):
      prompt = '>>>'

      def do_hello(self, line):
          print("Hello!", line)

     def do_quit(self, line):
         return True

if __name__ = __main__:
     MyCmd().cmdloop()


Int this example users can tyoe hello followed by anything else they want and "quit" whenever they want to quit the program. 

Welcome and please, if yiu see anything that you can do better than me, please make sure to let me know or you can just fork thr repository and make the changes.




