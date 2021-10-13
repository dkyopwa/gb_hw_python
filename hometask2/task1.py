#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    lst = [10, 12.3, 'str', [], (), {1, 2}, {'1':1, '2':2}, True, b'123', None]
    for item in lst:
        print(f'{item}: {type(item)}')
        