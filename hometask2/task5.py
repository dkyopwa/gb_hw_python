#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    while True:
        my_list = [7, 5, 3, 3, 2]

        number = input('Enter number or ENTER to stop: ')
        if not number:
            break

        flag = False
        for i in range(len(my_list)):
            if int(number) > my_list[i]:
                my_list.insert(i, int(number))
                flag = True
                break
        if not flag:
            my_list.append(int(number))

        print(my_list)
