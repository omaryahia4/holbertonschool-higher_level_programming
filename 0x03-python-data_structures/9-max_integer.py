#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in list(my_list):
        if my_list == 0:
            return None
        else:
            my_list.sort()
            return my_list[-1]
