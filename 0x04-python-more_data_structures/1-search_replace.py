#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list == [] or my_list is None:
        return []
    new = [replace if item is search else item for item in my_list]
    return new
