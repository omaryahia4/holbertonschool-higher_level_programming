#!/usr/bin/python3
"""Module to check for type of obj"""


def is_same_class(obj, a_class):
    """check obj if it's exactly an instance of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
