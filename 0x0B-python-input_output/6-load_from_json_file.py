#!/usr/bin/python3
"""
==================
import module json
==================
"""


import json


def load_from_json_file(filename):
    """read a file and return a json format"""

    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
