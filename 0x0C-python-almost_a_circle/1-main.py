#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)
    print(r1.width, r1.height, r1.x, r1.y)

    r2 = Rectangle(2, 10)
    print(r2.id)
    print(r2.width, r2.height, r2.x, r2.y)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
    print(r3.width, r3.height, r3.x, r3.y)
