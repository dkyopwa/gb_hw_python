#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    with open('task1.txt', 'w') as file:
        while True:
            str = input('Enter data (empty string to stop): ')
            if str == '':
                break
            file.write(str + '\n')
