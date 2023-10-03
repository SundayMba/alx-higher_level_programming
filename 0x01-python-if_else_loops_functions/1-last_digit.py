#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
las = (number * -1) % 10 if number < 0 else number % 10

if las == 0:
    print(f"Last digit of {number} is {las} and is 0")
elif number < 0 or las < 6:
    if number < 0:
        print(f"Last digit of {number} is -{las} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {las} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {las} and is greater than 5")
