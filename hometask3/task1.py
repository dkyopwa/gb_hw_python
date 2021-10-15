#!/usr/bin/env python
# nevl 2021

def func_div(arg1, arg2):
    """
    Function divide arg1 on arg1

    :param arg1: (float) numerator
    :param arg2: (float) denominator
    :return: (float) arg1 / arg2
    """
    if arg2 != 0.0:
        return arg1 / arg2
    return None


if __name__ == '__main__':
    number1 = float(input('Enter numerator: '))
    number2 = float(input('Enter denominator: '))

    print(func_div(number1, number2))
