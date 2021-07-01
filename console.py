#!/usr/bin/python3
"""
    contains entry point of command interpreter
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
        class HBNBCommand
    """
    all_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    def __init__(self):
        """
            prompts user
        """
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_create(self, line):
        """Creates a new BaseModel instance
        Args:
            None
        Prints id of the new BaseModel instance
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
        else:
            base1 = HBNBCommand.all_classes[line]()
            base1.save()
            print(base1.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id. Example: $ show BaseModel 1234-1234-1234.
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[ke_y]
                print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id. Example: (hbnb)  destroy BaseModel 1234-1234-1234.
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                del(all_instances[ke_y])
                storage.save()

    def do_all(self, line):
        """
        Prints the string representation of all instances
        Example: (hbnb) all BaseModel
        or (hbnb) all
        """
        obj_list = []
        all_list = []
        all_instances = storage.all()
        if line == "":
            for k, obj in all_instances.items():
                all_list.append(str(obj))
            print(all_list)
        elif line in HBNBCommand.all_classes.keys():
            for k, v in all_instances.items():
                if line == v.__class__.__name__:
                    ke_y = line + "." + str(v.id)
                    obj_list.append(all_instances[ke_y])
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). Ex: (hbnb)
        update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        elif len(a_list) == 2:
            print("** attribute name missing **")
        elif len(a_list) == 3:
            print("** value missing **")
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[ke_y]
                setattr(obj, a_list[2], a_list[3])
                storage.save()

    def help_quit(self):
        """
            handling help command
        """
        print('Quit command to exit the program')

    def emptyline(self):
        """
            Called when an empty line is entered
            in response to the prompt.
            If this method is not overridden,
            it repeats the last nonempty
            command entered.
        """
        pass

    def do_quit(self, arg):
        """
            quits the cli
        """
        raise SystemExit(0)

    def do_EOF(self, arg):
        """
            handles EOF
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
