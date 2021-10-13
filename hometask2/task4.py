#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    str = input('Enter string: ')
    for i, s in enumerate(str.split()):
        print(f'{i}: {s[:10]}')
