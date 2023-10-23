#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        idx = 0
        flag = 0
        while idx < x:
            if type(my_list[idx]) is int:
                print("{:d}".format(my_list[idx]), end="")
                idx += 1
            else:
                idx += 1
                flag += 1
        print()
        return idx - flag
    except IndexError:
        raise
