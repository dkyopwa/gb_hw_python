#!/usr/bin/env python
# nevl 2021

def my_func1(x, y):
    """
    Exponentiation v1

    :param x: float: Positive number
    :param y: int: Negative number
    :return: float: Exponentiation
    """
    return x ** y

def my_func2(x, y):
    """
    Exponentiation v1

    :param x: float: Positive number
    :param y: int: Negative number
    :return: float: Exponentiation
    """
    res = x
    for _ in range(abs(y) - 1):
        res *= x

    return 1.0 / res


if __name__ == '__main__':
    x = float(input('Enter x (positive): '))
    y = int(input('Enter y (negative int): '))
    if x < 0 or y > -1:
        print('Data is not correct.')
        quit(1)

    print(my_func1(x, y))
    print(my_func2(x, y))
