#!/usr/bin/env python
# nevl 2021

from itertools import cycle
from sys import argv

# a quoted list separated by spaces
lst = argv[1].split()
max_count = int(argv[2])

for i, it in enumerate(cycle(lst)):
    if i > max_count:
        break
    print(it)
