#!/usr/bin/env python
# nevl 2021

def fact(n):
    """
    Factorial

    :param n: int
    :return: int
    """
    if n < 1:
        return
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res

if __name__ == '__main__':
    n = int(input('Enter max: '))

    for el in fact(n):
        print(el)
