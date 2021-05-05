#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
        for x in range(len(my_list)):
            if my_list is not None:
                my_list.reverse()
                print("{:d}".format(my_list[x]))
