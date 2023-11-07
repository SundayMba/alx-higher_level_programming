#!/usr/bin/python3
"""
=========================
Modules for saving to json
=========================
"""


import json
import os.path
import sys
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""initialize your filename"""
filename = "add_item.json"
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

count = 1
for index in argv[count]:
    if argv[count] is None:
        count += 1
        continue
    json_list.append(index)
    count += 1

save_to_json_file(json_list, filename)
