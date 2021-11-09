#!/usr/bin/env python
# nevl 2021

class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date_int(cls, date):
        if not Date.is_date(date):
            return None

        s = date.split('-')
        if len(s) != 3:
            return None

        try:
            return int(f'{s[0]}{s[1]}{s[2]}')
        except:
            return None

    @staticmethod
    def is_date(date_str):
        date_data = ([str(c) for c in range(10)])
        date_data.append('-')

        # check symbols
        for c in date_str:
            if c not in date_data:
                return False

        # check format
        s = date_str.split('-')
        if len(s) != 3:
            return False

        for i, it in enumerate([2, 2, 4]):
            if len(s[i]) != it:
                return False

        # default
        return True


if __name__ == '__main__':
    date1 = '01-01-1970'
    date2 = '2020-02-02'

    for date in [date1, date2]:
        print(f'Valid date {date}: {Date.get_date_int(date)}' if Date.is_date(date) else f'Invalid date {date}')
