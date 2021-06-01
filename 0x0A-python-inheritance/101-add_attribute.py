#!/usr/bin/python3
"""add attribute"""


def add_attribute(obj, name, value):
    """adds a new attribute if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
