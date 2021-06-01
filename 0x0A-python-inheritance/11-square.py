#!/usr/bin/python3
"""Module Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """inisialisation of square class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of the square"""
        return self.__size**2

    def __str__(self):
        """str function"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
