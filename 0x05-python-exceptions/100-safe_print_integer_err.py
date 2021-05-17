#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value, end=""))
        return True
    except:
        print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
        return False
