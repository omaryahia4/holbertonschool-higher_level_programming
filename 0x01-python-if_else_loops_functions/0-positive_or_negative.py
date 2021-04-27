#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive\n".format(number))
elif number == 0:
    print("{:d} is zero\n".format(number))
else:
    print("{:d} is negative\n".format(number))
