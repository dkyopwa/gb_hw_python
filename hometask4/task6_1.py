#!/usr/bin/env python
# nevl 2021

from itertools import count
from sys import argv

start = int(argv[1])
max_count = int(argv[2])

for i in count(start):
    if i > max_count:
        break
    print(i)
