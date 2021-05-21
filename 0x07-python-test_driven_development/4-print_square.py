#!/usr/bin/python3
"""
This module is composed by a function that prints a square with the character #
"""


def print_square(size):
    """ Function that prints a square with the character #
    Args:
        size: size of the square printed
    Returns:
        No return
    Raises:
        TypeError: If size is not an integer number
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        print ('#' * size)
