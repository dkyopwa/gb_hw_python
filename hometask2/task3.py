#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    months_list = ['winter', 'winter',
                   'spring', 'spring', 'spring',
                   'summer', 'summer', 'summer',
                   'autumn', 'autumn', 'autumn',
                   'winter']
    months_dict = {
        1: 'winter',
        2: 'winter',
        3: 'spring',
        4: 'spring',
        5: 'spring',
        6: 'summer',
        7: 'summer',
        8: 'summer',
        9: 'autumn',
        10: 'autumn',
        11: 'autumn',
        12: 'winter'
    }

    month = int(input('Enter month number: '))
    print(months_list[month - 1])
    print(months_dict[month])
