#!/usr/bin/env python3
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """
        creates new instance of basemodel
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        prints the string representation of instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            instances = storage.all()
            key = class_name + "." + instance_id
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        prints all string reps of all instances
        """
        args = arg.split()
        if len(args) == 0 or args[0] not in storage.classes:
            print([str(obj) for obj in storage.all().values()])
        else:
            print([str(obj) for obj in storage.all().values() if
                   obj.__class__.__name__ == arfs[0]])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
