#!/usr/bin/python3
""" Console Module """
import cmd
from models.city import City
from models.amenity import Amenity
from models.review import Review
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ determines the functionality of the HBNB console that we are constantly improving"""

    # defining the command prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel,
               'User': User,
               'Place': Place,
               'State': State,
               'City': City, 
               'Amenity': Amenity,
               'Review': Review
              }

    accessed_via_dot = ['all', 'count', 'show', 'destroy', 'update']

    types = {
             'number_rooms': int,
             'number_bathrooms': int,
             'max_guest': int,
             'price_by_night': int,
             'latitude': float,
             'longitude': float
            }

    def preloop(self):
        """Prints the loop if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def do_quit(self, command):
        """function to quit the console"""
        exit()

    def help_quit(self):
        """ Tells us more about the quit function """
        print("Exits the program with formatting\n")

    def emptyline(self):
        """  function will Overrides the emptyline method of CMD """
        pass

    def do_EOF(self, arg):
        """ function Handles EOF to exit program """
        print()
        exit()

    def precmd(self, line):
        """function reformats command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**the_key_word_args>]])
        (Brackets denote optional fields in usage example.)
        """
        _the_defined_command = _the_defined_class = _the_defined_ID = _args = ''

        # scan for general formatting - that is '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            parse_the_line = line[:]  # parsed line

            #isolate <class name>
            _the_defined_class = parse_the_line[:parse_the_line.find('.')]

            #isolate and validate <command>
            _the_defined_command = parse_the_line[parse_the_line.find('.') + 1:parse_the_line.find('(')]
            if _the_defined_command not in HBNBCommand.accessed_via_dot:
                raise Exception

            # if parantheses contain arguments, parse them
            parse_the_line = parse_the_line[parse_the_line.find('(') + 1:parse_the_line.find(')')]
            if parse_the_line:
                # partition args: (<id>, [<delim>], [<*args>])
                # parse_the_line convert to tuple
                parse_the_line = parse_the_line.partition(', ')

                # isolate _the_defined_ID, stripping quotes
                _the_defined_ID = parse_the_line[0].replace('\"', '')
                # there might be a possible bug here:
                # empty quotes register as empty _the_defined_ID when replaced

                # if arguments exist beyond _the_defined_ID
                parse_the_line = parse_the_line[2].strip()  # parse_the_line is now str
                if parse_the_line:
                    # check for *args or **the_key_word_args
                    if parse_the_line[0] == '{' and parse_the_line[-1] == '}'\
                            and type(eval(parse_the_line)) is dict:
                        _args = parse_the_line
                    else:
                        _args = parse_the_line.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_the_defined_command, _the_defined_class, _the_defined_ID, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_create(self, args):
        """ function to create an object of any class"""
        try:
            if not args:
                raise SyntaxError()
            arg_list = args.split(" ")
            the_key_word = {}
            for arg in arg_list[1:]:
                the_arg_splitted = arg.split("=")
                the_arg_splitted[1] = eval(the_arg_splitted[1])
                if type(the_arg_splitted[1]) is str:
                    the_arg_splitted[1] = the_arg_splitted[1].replace("_", " ").replace('"', '\\"')
                the_key_word[the_arg_splitted[0]] = the_arg_splitted[1]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        latest_instance = HBNBCommand.classes[arg_list[0]](**the_key_word)
        latest_instance.save()
        print(latest_instance.id)

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """function shows individual objects """
        the_new = args.partition(" ")
        precise_name = the_new[0]
        precise_defined_ID = the_new[2]

        # guard against trailing args
        if precise_defined_ID and ' ' in precise_defined_ID:
            precise_defined_ID = precise_defined_ID.partition(' ')[0]

        if not precise_name:
            print("** class name missing **")
            return

        if precise_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not precise_defined_ID:
            print("** instance id missing **")
            return

        key = precise_name + "." + precise_defined_ID
        try:
            print(storage._FileStorage__objects[key])
        except keyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        the_new = args.partition(" ")
        precise_name = the_new[0]
        precise_defined_ID = the_new[2]
        if precise_defined_ID and ' ' in precise_defined_ID:
            precise_defined_ID = precise_defined_ID.partition(' ')[0]

        if not precise_name:
            print("** class name missing **")
            return

        if precise_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not precise_defined_ID:
            print("** instance id missing **")
            return

        key = precise_name + "." + precise_defined_ID

        try:
            del(storage.all()[key])
            storage.save()
        except keyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all(HBNBCommand.classes[args]).items():
                print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))
        print(print_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a certain object with the_new info """
        precise_name = precise_defined_ID = attribute_name = attribute_value = the_key_word_args = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            precise_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if precise_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            precise_defined_ID = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = precise_name + "." + precise_defined_ID

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if the_key_word_args or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            the_key_word_args = eval(args[2])
            args = []  # reformat the_key_word_args into list, ex: [<name>, <value>, ...]
            for k, v in the_key_word_args.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                the_second_quote = args.find('\"', 1)
                attribute_name = args[1:the_second_quote]
                args = args[the_second_quote + 1:]

            args = args.partition(' ')

            # if attribute_name was not quoted arg
            if not attribute_name and args[0] != ' ':
                attribute_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                attribute_value = args[2][1:args[2].find('\"', 1)]

            # if attribute_value was not quoted arg
            if not attribute_value and args[2]:
                attribute_value = args[2].partition(' ')[0]

            args = [attribute_name, attribute_value]

        # retrieve dictionary of current objects
        the_new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, attribute_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                attribute_value = args[i + 1]  # following item is value
                if not attribute_name:  # check for attribute_name
                    print("** attribute name missing **")
                    return
                if not attribute_value:  # check for attribute_valueue
                    print("** value missing **")
                    return
                # type cast as necessary
                if attribute_name in HBNBCommand.types:
                    attribute_value = HBNBCommand.types[attribute_name](attribute_value)

                # update dictionary with name, value pair
                the_new_dict.__dict__.update({attribute_name: attribute_value})

        the_new_dict.save()  # save updates to file

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with the_new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
