#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value, end=""))
        return True
    except (NameError, TypeError) as eroor:
        print("Exception: {}".format(eroor), file=sys.stderr)
        return False
