#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    lst = input('Enter numbers separated by spaces: ').split()
    new_lst = (it for it in lst)

    tmp = dict()
    res = list()

    for it in new_lst:
        if it in tmp:
            tmp[it] += 1
        else:
            tmp[it] = 1

    for key, value in tmp.items():
        if value == 1:
            res.append(key)

    print(res)
