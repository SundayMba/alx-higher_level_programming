#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    size = len(argv)
    if size == 1:
        print(0)
    else:
        new = [int(item) for item in argv if item != argv[0]]
        print(sum(new))
