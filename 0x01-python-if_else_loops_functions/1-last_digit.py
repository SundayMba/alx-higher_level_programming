#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = (number * -1) % 10 if number < 0 else number % 10

if last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif number < 0 or last < 6:
    if number < 0:
        print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last} and is greater than 5")

