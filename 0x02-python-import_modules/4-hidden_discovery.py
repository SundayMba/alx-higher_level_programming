#!/usr/bin/python3

import hidden_4.pyc as sys

if __name__ == "__main__":
    items = dir(sys)
    for item in items:
        if '__' not in item:
            print(item)
