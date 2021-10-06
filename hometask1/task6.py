#!/usr/bin/env python
# nevl 2021

def is_int(str):
    try:
        tmp = int(str)
        if tmp <= 0:
            print('Input positive number.')
        return True
    except:
        print('Input not a number')
    return False

if __name__ == '__main__':
    # fetch proceeds
    while True:
        a = input('Input a: ')
        if is_int(a):
            break

    # fetch costs
    while True:
        b = input('Input b: ')
        if is_int(b):
            break

    count = 1
    distance = float(a)
    while distance < int(b):
        distance += distance * 0.1
        count += 1

    print(count)
