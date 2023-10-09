#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = [x for x in my_list]
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return my_list
