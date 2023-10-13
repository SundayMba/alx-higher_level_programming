#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, key_value in a_dictionary.copy().items():
        if key_value == value:
            del a_dictionary[key]
    return a_dictionary
