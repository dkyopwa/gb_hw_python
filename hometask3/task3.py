#!/usr/bin/env python
# nevl 2021

def my_func(arg1, arg2, arg3):
    """
    The sum of the largest two arguments

    :param arg1: float: Argument 1
    :param arg2: float: Argument 2
    :param arg3: float: Argument 3
    :return: float: sum
    """
    maxs = [arg1, arg2, arg3]
    maxs.sort(reverse=True)
    return maxs[0] + maxs[1]


if __name__ == '__main__':
    number = list()
    for _ in range(3):
        number.append(float(input('Enter number: ')))

    print(my_func(number[0], number[1], number[2]))
