#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    # fetch number and check
    while True:
        tmp = input('Input number: ')
        try:
            tmp = int(tmp)
            if tmp < 0 or tmp > 9:
                print('Enter only one symbol.')
                continue
            else:
                break
        except:
            print('Not a number. Try again.')
            continue

    # make new numbers in strings
    s2 = f'{tmp}'*2
    s3 = f'{tmp}'*3

    # calculate
    print(tmp + int(s2) + int(s3))
