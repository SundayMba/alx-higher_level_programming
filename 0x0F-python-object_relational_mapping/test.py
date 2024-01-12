#!/usr/local/bin/python3

import sys
import re

text = sys.argv[1]
pattern = re.compile(r'^[a-zA-Z]+', re.I)
matches = pattern.findall(text)
print(matches[0])
