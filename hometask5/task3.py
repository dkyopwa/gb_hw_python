#!/usr/bin/env python
# nevl 2021

if __name__ == '__main__':
    employes = dict()
    with open('task3.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            t = line.split()
            employes[t[0]] = int(t[1])
            if int(t[1]) < 20000:
                print(f'{t[0]}\t{t[1]}')

    print(sum(employes.values()) / len(employes.values()))
