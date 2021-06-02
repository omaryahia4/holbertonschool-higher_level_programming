#!/usr/bin/python3
"""number of lines"""


def write_file(filename="", text=""):
    """Writes a string to a file and returns number of characters"""
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
