#!/usr/bin/python3

def no_c(my_string):
    new_str = []
    for string in my_string:
        if string not in 'cC':
            new_str.append(string)
    return ''.join(new_str)
