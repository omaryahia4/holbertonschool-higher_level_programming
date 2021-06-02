#!/usr/bin/python3
def write_file(filename="", text=""):
    """Writes a string to a file and returns number of characters"""
    with open(filename, 'w', encoding="UTF8") as f:
        return len(text)
