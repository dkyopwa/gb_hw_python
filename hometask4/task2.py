#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    lst = input('Enter numbers separated by space: ').split()
    new_lst = (it for it in lst)

    res = list()
    prev = next(new_lst)
    for item in new_lst:
        if float(item) > float(prev):
            res.append(item)
        prev = item

    print(res)
