#!/usr/bin/python3
"""Module base """

import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method that returns the JSON string
         representation of list_dictionaries"""

        if list_dictionaries is None or not list_dictionaries:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        file_name = cls.__name__ + ".json"
        dict = []
        if list_objs is not None:
            for i in list_objs:
                dict.append(cls.to_dictionary(i))
        with open(file_name, 'w') as file:
            file.write(cls.to_json_string(dict))

    @staticmethod
    def from_json_string(json_string):
        """ static method that deserializes json_string """
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ class method that returns
        an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
