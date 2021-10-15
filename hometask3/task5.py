#!/usr/bin/env python
# nevl 2021

def is_number(str):
    """
    Сhecking a string for a number

    :param str: String: Users input
    :return: True/False
    """
    try:
        float(str)
        return True
    except:
        return False


if __name__ == '__main__':
    result = 0.0
    end_flag = False
    while not end_flag:
        str = input('Enter numbers separated by a space or a letter to interrupt input: ')

        lst = str.split()
        for it in lst:
            if is_number(it):
                result += float(it)
            else:
                end_flag = True
                break

        print(result)
