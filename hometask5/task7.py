#!/usr/bin/env python
# nevl 2021

import json

if __name__ == '__main__':
    i = 0
    result = dict()
    total_profit = 0.0

    with open('task7.txt', 'r') as file:
        while True:
            # read file by line
            line = file.readline()
            if not line:
                break

            # split line
            data = line.split()
            # calculate
            profit = int(data[2]) - int(data[3])
            result[data[0]] = profit
            if profit > 0:
                total_profit += profit
                # positive profit company counter
                i += 1

    # calculate average_profit
    average_profit = {'average_profit':total_profit/i if i else 1}

    with open('task7_new.txt', 'w') as file:
        json.dump([result, average_profit], file)
