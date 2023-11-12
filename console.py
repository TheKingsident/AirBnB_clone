#!/usr/bin/python3
"""
The console module
"""
import cmd
import re
from models import amenity, base_model, place, review, user, state, city
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNBCommand shell."""
    intro = 'Welcome to the HBNBCommand shell. Type help to list commands.\n'
    prompt = '(hbnb) '

    classes = {
        'BaseModel': base_model.BaseModel,
        'User': user.User,
        'State': state.State,
        'City': city.City,
        'Amenity': amenity.Amenity,
        'Place': place.Place,
        'Review': review.Review
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, inp):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, line):
        "Exit the command interpreter"
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON
            file, and prints the id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Shows all objects/instances
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if len(args) < 2:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
            return

        class_name, instance_id = args
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        key = f"{class_name}.{instance_id}"

        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and ID
        """
        args = arg.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        else:
            print([str(obj) for key, obj in all_objs.items()
                   if key.startswith(args[0])])

    def do_destroy(self, arg):
        """deletes an instance based on the class
        name and ID, and then saves the change."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if len(args) < 2:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
            return

        class_name, instance_id = args
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        key = f"{class_name}.{instance_id}"

        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """It updates"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if len(args) < 2:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        class_name, instance_id, attribute_name, attribute_value = args[:4]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        key = f"{class_name}.{instance_id}"

        if key not in all_objs:
            print("** no instance found **")
            return

        instance = all_objs[key]
        if attribute_name in ['id', 'created_at', 'updated_at']:
            return

        try:
            attribute_value = eval(attribute_value)
        except (SyntaxError, NameError):
            # Assume it's a string and leave as is
            pass

        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def default(self, line):
        """
        Default behavior for unrecognized commands, enabling additional syntax.
        """
        pattern_all = r"^\w+\.all\(\)$"
        pattern_count = r"^\w+\.count\(\)$"

        if re.match(pattern_all, line):
            class_name = line.split(".")[0]
            if class_name in self.classes:
                self.do_all(class_name)
            else:
                print("** class doesn't exist **")
        elif re.match(pattern_count, line):
            class_name = line.split(".")[0]
            self.do_count(class_name)
        else:
            print(f"*** Unknown syntax: {line}")

    def do_count(self, class_name):
        """
        Count the number of instances of a given class name.
        """
        if class_name in self.classes:
            all_objs = storage.all()
            count = sum(1 for key in all_objs if key.startswith(
                                                        class_name + "."))
            print(count)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
