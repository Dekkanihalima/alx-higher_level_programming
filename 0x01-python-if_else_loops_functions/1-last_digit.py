#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
msg1 = " and is greater than 5"
msg2 = " and is 0"
msg3 = " and is less than 6 and not 0"
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
if last_digit > 5:
    print("Last digit of {} is {}".format(number, last_digit) + msg1)
elif last_digit == 0:
    print("Last digit of {} is {}".format(number, last_digit) + msg2)
else:
    print("Last digit of {} is {}".format(number, last_digit) + msg3)
