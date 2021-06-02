#!/usr/bin/python3
"""append text"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file"""
    with open(filename, "a+", encoding="UTF8") as f:
        f.write(text)
        return len(text)
