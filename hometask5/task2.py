#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    i = 0
    with open('task2.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            i += 1
            count = line.strip().split()
            print(f'{i}: {len(count)} words')

    print(f'There are {i} lines')
