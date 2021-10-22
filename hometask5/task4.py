#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    data = dict()
    with open('task4.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            t = line.split()
            data[t[0]] = int(t[2])

    numbers = {
        'One':'Один',
        'Two':'Два',
        'Three':'Три',
        'Four':'Четыре'
    }

    with open('task4_new.txt', 'w') as file:
        for it in data.keys():
            file.write(f'{numbers[it]} - {data[it]}\n')
