#!/usr/bin/python3
def no_c(my_string):
    bad_chars = ['c', 'C']
    my_string = ''.join((filter(lambda i: i not in bad_chars, my_string)))
    return my_string
