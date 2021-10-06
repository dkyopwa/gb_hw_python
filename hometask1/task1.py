#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    # variables
    test_int = 1
    test_float = 1.1
    test_str = 'String'
    test_bool = True
    test_list = [1, 2]
    test_tuple = (3, 4)
    test_dict = {
        "first": 1,
        "second": 2
    }

    # print section
    print(test_int)
    print(test_float)
    print(test_str)
    print(test_bool)
    print(test_list)
    print(test_tuple)
    print(test_dict)

    # input section
    tmp_str = input('Write string: ')
    print(tmp_str, type(tmp_str))
    tmp_int = input('Write integer: ')
    print(tmp_int, type(tmp_int))
    tmp_float = input('Write float: ')
    print(tmp_float, type(tmp_float))

    print('Done')
