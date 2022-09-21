#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lsg = (((-1 * number) % 10) * -1)
else:
    lsg = number % 10
if lsg > 5:
    print(f"Last digit of {number} is {lsg} and is greater than 5")
elif lsg == 0:
    print(f"Last digit of {number} is {lsg} and is 0")
elif lsg < 6 and lsg != 0:
    print(f"Last digit of {number} is {lsg} and is less than 6 and not 0")
