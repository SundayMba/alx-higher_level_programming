#!usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        while idx < x:
            print(my_list[idx], end="")
            idx += 1
        print()
        return idx
    except IndexError:
        print()
        return idx
