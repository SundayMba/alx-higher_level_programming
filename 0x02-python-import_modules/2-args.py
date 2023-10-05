#!/usr/bin/python3

import sys

if __name__ == "__main__":
    size = len(sys.argv)
    if size == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(size - 1))
        size = 0
        for item in sys.argv:
            if size != 0:
                print("{}: {}".format(size, sys.argv[size]))
            size += 1
