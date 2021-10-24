#!/usr/bin/env python
# nevl 2021

class Road:
    __length = 0.0
    __width = 0.0

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc(self, depth=1):
        return self.__length * self.__width * 25 * depth / 1000.0


if __name__ == '__main__':
    road = Road(5000, 20)
    print(road.calc(5))
