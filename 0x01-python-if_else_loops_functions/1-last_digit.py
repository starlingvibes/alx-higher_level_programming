#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

pre = "Last digit of "
if number < 0:
    last_digit = -(abs(number) % 10)
else:
    last_digit = number % 10
if last_digit > 5:
    print(f"{pre:s}{number:d} is {last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"{pre:s}{number:d} is {last_digit:d} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"{pre:s}{number:d} is {last_digit:d} and is less than 6 and not 0")
