#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (IndexError, ZeroDivisionError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        result = None
    return result