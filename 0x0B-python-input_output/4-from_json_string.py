#!/usr/bin/python3
import json
"""import JSON (JavaScript Object Notation)"""


def from_json_string(my_str):
    """ returns an object (Python data structure)
    represented by a JSON string"""
    return json.loads(my_str)
