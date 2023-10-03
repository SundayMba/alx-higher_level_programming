#!/usr/bin/python3
for outer in range(0, 9):
    for inner in range(outer + 1, 10):
        if outer == 8 and inner == 9:
            print("{:d}{:d}".format(outer, inner))
        else:
            print("{:d}{:d},".format(outer, inner), end=" ")
