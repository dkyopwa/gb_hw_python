#!/usr/bin/env python
# nevl 2021

class NewException(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    while True:
        n1 = input('Enter first number or press ENTER to complete input: ')
        n2 = input('Enter second number or press ENTER to complete input: ')
        if not n1 or not n2:
            break
        try:
            n1 = float(n1)
            n2 = float(n2)
        except Exception as e:
            print(e)
            continue

        try:
            if n2 == 0:
                raise NewException('Division by zero')
            print(f'Division result {n1 / n2}')
        except NewException as e:
            print(e)
        except Exception as e:
            print(e)
