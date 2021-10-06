#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    # fetch count of seconds and check for number
    while True:
        tmp = input('Input seconds: ')
        try:
            tmp = int(tmp)
            break
        except:
            print('Input not a number')

    # calculate time
    hours = tmp // 3600
    minutes = (tmp - (hours * 3600)) // 60
    seconds = tmp % 60
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
