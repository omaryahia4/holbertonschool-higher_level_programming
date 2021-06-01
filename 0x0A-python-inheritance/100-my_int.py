#!/usr/bin/python3
"""Myint"""


class MyInt(int):
    """ MyInt Class """

    def __eq__(self, other):
        """__eq__ Method"""
        return int(self) != int(other)

    def __ne__(self, other):
        """__ne__ Method"""
        return int(self) == int(other)
