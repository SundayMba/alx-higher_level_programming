#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    size = len(argv)
    if size == 1:
        print("0 arguments.")
    else:
        if size == 2:
            print("{} argument:".format(size - 1))
        else:
            print("{} arguments:".format(size - 1))
        size = 0
        for item in argv:
            if size != 0:
                print("{}: {}".format(size, argv[size]))
            size += 1
