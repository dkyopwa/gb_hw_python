#!/usr/bin/env python
# nevl 2021

import re

if __name__ == '__main__':
    subjects = dict()

    with open('task6.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.split(':')
            nums = re.findall(r'\d+', data[1])
            subjects[data[0]] = sum(int(n) for n in nums)

    print(subjects)
