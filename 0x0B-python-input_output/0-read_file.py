#!/usr/bin/python3
"""
==================
module 0-read_file
==================
"""


def read_file(filename=""):
    """function to open a file"""

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
