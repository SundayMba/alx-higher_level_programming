#!/usr/bin/python3

""" Base module """


class Base:
    """ Base Class for for all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor for the base class

            it is only the class that has read/write access to the class
            attribute, but the instance (self) has only read access to the
            class attribute. not write access. so the instance (self) cannot
            modify the class attribute.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert from list of dictionaries to json string """
        if list_dictionaries is None:
            return '"[]"'
        if list_dictionaries == []:
            return "\"[]\""
        return str(list_dictionaries).replace("'", '"')

    @classmethod
    def save_to_file(cls, list_objs):
        """ save a list of objects to a file """
        if list_objs is None:
            json_list = "[]"
            file_name = f"{cls.__name__}.json"
        else:
            """ create a list of json string """
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_list = Base.to_json_string(dict_list)
            file_name = f'{cls.__name__}.json'
        with open(file_name, 'w') as file:
            file.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """ from json string to dictionary """
        import json
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ dictionary to instance converter """
        if cls.__name__.lower() == "square":
            from models.square import Square as obj
        else:
            from models.rectangle import Rectangle as obj
        dummy = obj(3, 4)
        """ it is received as a dictionary, it must be unbound back to
            key/value pair before given to update with the real values
        """
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load a json string from a given file and convert """
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, 'r') as file:
                json_content = file.read()
                obj_list = Base.from_json_string(json_content)
                if obj_list == []:
                    return []
                list_instance = []
                for obj in obj_list:
                    instance = cls.create(**obj)
                    list_instance.append(instance)
                return list_instance
        except Exception:
            return []
