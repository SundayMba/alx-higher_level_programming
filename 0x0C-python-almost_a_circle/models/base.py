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
            return "[]"
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
            dummy = obj(3)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save the object formatted data to the file in csv format"""
        filename = f'{cls.__name__}.csv'
        data = ''
        if list_objs is None:
            data = ''
        else:
            if cls.__name__ == 'Square':
                for obj in list_objs:
                    data += f'{obj.id},{obj.width},{obj.x},{obj.y},'
            else:
                for ob in list_objs:
                    data += f"{ob.id},{ob.width},{ob.height},{ob.x},{ob.y},"
            data = data.removesuffix(',')
        with open(filename, 'w') as file:
            file.write(data)

    @classmethod
    def load_from_file_csv(cls):
        """ load a csv from file and convert them to the given object """
        try:
            index = 0
            list_s = []
            filename = f'{cls.__name__}.csv'
            with open(filename, 'r') as file:
                data = file.read()
                n = ' '.join(data.split(',')).rstrip().split(' ')
                if cls.__name__ == "Square":
                    len_s = len(n) // 4
                    s = {}
                    while len_s > 0:
                        s['id'] = int(n[index])
                        s['size'] = int(n[index+1])
                        s['x'] = int(n[index+2])
                        s['y'] = int(n[index+3])
                        index += 4
                        list_s.append(cls.create(**s))
                        len_s -= 1
                    return list_s
                len_s = len(n) // 5
                s = {}
                index = 0
                while len_s > 0:
                    s['id'] = int(n[index])
                    s['width'] = int(n[index+1])
                    s['height'] = int(n[index+2])
                    s['x'] = int(n[index+3])
                    s['y'] = int(n[index+4])
                    list_s.append(cls.create(**s))
                    index += 5
                    len_s -= 1
                return list_s
        except Exception as e:
            return ''
