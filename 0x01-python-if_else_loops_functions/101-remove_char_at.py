#!/usr/bin/python3

def remove_char_at(str, n):
    new = []
    for i in range(0, len(str)):
        if i != n:
            new.append(str[i])
    return "".join(new)
