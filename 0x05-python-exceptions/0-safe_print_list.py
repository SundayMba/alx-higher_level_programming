#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    idx = 0
    try:
        while idx < x:
            print("{}".format(my_list[idx]), end="")
            idx += 1
        print()
        return idx
    except IndexError:
        print()
        return idx
