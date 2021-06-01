#!/usr/bin/python3
"""Inheritance from a list"""


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """sorted list"""
        print(sorted(self))
