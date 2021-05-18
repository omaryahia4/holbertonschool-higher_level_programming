#!/usr/bin/python3
"""Module Square"""


class Square:
    """ Square class """
    def __init__(self, size=0):
        """Initializes the data

        Args:
            size (int): size of square
        """
        self.__size = size

    def area(self):
        """The square's square area"""
        self.area = self.__size ** 2
        return int(self.area)

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
