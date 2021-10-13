#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    lst = list()
    while True:
        el = input('Enter an item or press ENTER to complete input: ')
        if not el:
            break
        lst.append(el)

    print(lst)

    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]

    print(lst)
