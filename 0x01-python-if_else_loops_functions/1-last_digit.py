#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = int(repr(number)[-1])
if x > 5:
	print("Last digit of {0} is {1} and is greater than 5\n".format(number, x))
elif x == 0:
	print("Last digit of {0} is {1} and is 0\n".format(number, x))
else:
	print("Last digit of {0} is {1} and is less than 6 and not 0\n".format(number, x))