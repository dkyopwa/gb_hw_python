#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    # fetch number and check
    while True:
        tmp = input('Input number: ')
        try:
            tmp = int(tmp)
            if tmp <= 0:
                print('Input positive number.')
                continue
            break
        except:
            print('Input not a number')

    # find the biggest number
    number = 0
    while tmp > 0:
        t = tmp % 10
        if t > number:
            number = t
        tmp //= 10

    print(f'The biggest number is: {number}')
