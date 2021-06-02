#!/usr/bin/python3
"""Module Student"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Student instance to JSON"""
        return self.__dict__
