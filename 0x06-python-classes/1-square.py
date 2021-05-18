#!/usr/bin/python3
""" Module Square """


class Square:
    """Represents a square with Private instance attribute size.

        Attribute:
            size (int): size of suare
    """

    def __init__(self, size):
        """Initializes the data

        Args:
            size (int): size of square
        """
        self.__size = size
