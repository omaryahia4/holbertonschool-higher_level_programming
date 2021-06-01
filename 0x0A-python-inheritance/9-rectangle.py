#!/usr/bin/python3
"""DModule Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """inisialisation of a rectangle class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """str format function"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
