#!/usr/bin/env python
# nevl 2021

import random

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, color, name, is_police=False):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = random.randint(1, 100)
        print(f'Car {self.name} ({self.color}) is going')

    def stop(self):
        self.speed = 0
        print(f'Car {self.name} ({self.color}) is staying')

    def turn(self, direction):
        if self.speed:
            print(f'Car {self.name} ({self.color}) turned to the {direction}')
        else:
            print(f'Car {self.name} ({self.color}) is staying')

    def show_speed(self):
        if self.speed <= 0:
            print(f'Car {self.name} ({self.color}) is staying. Speed 0 km/h')
        print(f'Speed car {self.name} ({self.color}) is {self.speed} km/h')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Over speed ')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Over speed ')


class PoliceCar(Car):
    def __init__(self, color, name, is_police=True):
        super().__init__(color, name, is_police)


if __name__ == '__main__':
    tc = TownCar('red', 'Mazda')
    tc.go()
    tc.show_speed()
    tc.turn('right')
    tc.stop()
    tc.show_speed()
    print('-' * 30)

    sc = SportCar('blue', 'Nissan GTR')
    sc.go()
    sc.show_speed()
    sc.turn('left')
    sc.stop()
    sc.show_speed()
    print('-' * 30)

    wc = WorkCar('grey', 'MAZ')
    wc.go()
    wc.show_speed()
    wc.turn('left')
    wc.stop()
    wc.show_speed()
    print('-' * 30)


    pc = PoliceCar('white', 'Mercedes')
    pc.go()
    pc.show_speed()
    pc.turn('left')
    pc.stop()
    pc.show_speed()
    print('-' * 30)
