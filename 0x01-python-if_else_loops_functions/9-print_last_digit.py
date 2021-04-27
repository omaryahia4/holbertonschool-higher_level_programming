#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    x = number % 10
    print(x, end='')
    return x
    