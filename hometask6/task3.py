#!/usr/bin/env python
# nevl 2021

class Worker:
    name = ''
    surname = ''
    position = ''
    __income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income['wage'] = wage
        self.__income['bonus'] = bonus

    def get_income(self):
        return self.__income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        income = self.get_income()
        return income['wage'] + income['bonus']


if __name__ == '__main__':
    pos = Position('John', 'Doe', 'plumber', 20000, 500)
    print(pos.get_full_name())
    print(pos.get_total_income())
