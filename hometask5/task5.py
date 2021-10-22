#!/usr/bin/env python
# nevl 2021

import random

if __name__ == '__main__':
    with open('task5.txt', 'w+') as file:
        for _ in range(100):
            file.write(f'{random.randint(0, 100)} ')

        file.seek(0)
        data = [int(i) for i in file.read().split()]
        print(sum(data))
        