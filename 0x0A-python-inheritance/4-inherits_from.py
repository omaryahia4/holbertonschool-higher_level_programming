#!/usr/bin/python3
""""Module to check for inhertiance"""


def inherits_from(obj, a_class):
    """ check for subclasses """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
