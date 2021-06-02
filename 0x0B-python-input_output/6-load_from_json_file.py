#!/usr/bin/python3
""""import JSON (JavaScript Object Notation)"""
import json


def load_from_json_file(filename):
    """load from JSON file"""
    with open(filename, encoding="UTF8") as f:
        return json.load(f)
