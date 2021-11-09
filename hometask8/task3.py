#!/usr/bin/env python
# nevl 2021

class NotNumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


def is_number(value):
    data = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']
    for s in value:
        if not s in data:
            raise NotNumberException('Entering value isn\'t number')
    if value.find('-') > 0 or value.count('.') > 1:
        raise NotNumberException('Entering value isn\'t number')

    return value


if __name__ == '__main__':
    l = list()

    while True:
        t = input('Enter number/string or press ENTER to complete input: ')
        if not t:
            break
        try:
            l.append(is_number(t))
        except NotNumberException as e:
            print(e)

    print(l)
