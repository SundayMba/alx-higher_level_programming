#!/usr/bin/python3
"""
=====================
importing module json
=====================
"""


import json


def to_json_string(my_obj):
    """return the jason repr of an obj"""

    return json.dumps(my_obj)
