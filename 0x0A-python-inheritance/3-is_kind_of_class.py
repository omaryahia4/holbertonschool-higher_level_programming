#!/usr/bin/python3
"""Module to check for type of obj"""


def is_kind_of_class(obj, a_class):
    """check obj if it's exactly an instance of the
    specified class or from a class that is inherited from"""
    return isinstance(obj, a_class)
