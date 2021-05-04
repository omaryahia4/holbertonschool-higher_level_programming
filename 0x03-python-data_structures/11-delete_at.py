#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in list(my_list):
        if idx < 0 or idx >= len(my_list):
            return my_list
        elif idx == i:
            my_list.remove(idx + 1)
    return my_list