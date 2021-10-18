#!/usr/bin/env python
# nevl 2021

from sys import argv

if __name__ == '__main__':
    script_name, production_in_hours, rate_per_hour, premium = argv
    print(f'{float(production_in_hours) * float(rate_per_hour) + float(premium)}')
