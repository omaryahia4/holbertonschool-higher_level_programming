#!/usr/bin/python3
"""Module Base Geometry"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Raise an Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True
