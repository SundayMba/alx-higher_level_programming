#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    name = ''
    max_score = -999999999999999999999  # an arbitrary selected number
    for student, score in a_dictionary.items():
        if score > max_score:
            name = student
            max_score = score
    return name
