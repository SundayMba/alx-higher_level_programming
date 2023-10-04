#!/usr/bin/python3

for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 != 0:
        upper = ord('A') + (c - ord('a'))
        print("{:c}".format(upper), end='')
    else:
        print("{}".format(chr(c)), end="")
