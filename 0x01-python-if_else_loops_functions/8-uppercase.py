#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        i = ord(ch)
        if (i <= 122 and i >= 97):
            i = i - 32
        print("{:c}".format(i), end="")
    print("")
