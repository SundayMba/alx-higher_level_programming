#!/usr/bin/python3
"""
=====================
importing module json
=====================
"""


import json


def from_json_string(my_str):
    """return an obj repr by a json string"""

    return json.loads(my_str)
