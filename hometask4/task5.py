#!/usr/bin/env python
# nevl 2021

from functools import reduce

if __name__ == '__main__':
    lst = [i for i in range(100, 1001, 2)]

    print(reduce(lambda prev, curr: prev * curr, lst))
