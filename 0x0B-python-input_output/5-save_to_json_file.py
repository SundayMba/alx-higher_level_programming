#!/usr/bin/python3
"""
===================
import module json
===================
"""


import json


def save_to_json_file(my_obj, filename):
    """return an obj repr by json string"""

    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
