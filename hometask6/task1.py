#!/usr/bin/env python
# nevl 2021

import time

class TrafficLight:
    __color = 'red'

    def running(self):
        print('TrafficLight running')
        for _ in range(10):
            if self.__color == 'red':
                for i in range(7, 0, -1):
                    print(f'\rred (7): {i}', end='')
                    time.sleep(1)
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                for i in range(2, 0, -1):
                    print(f'\ryellow (2): {i}', end='')
                    time.sleep(1)
                self.__color = 'green'
            elif self.__color == 'green':
                for i in range(10, 0, -1):
                    print(f'\rgreen (10): {i}', end='')
                    time.sleep(1)
                self.__color = 'red'
        print('TrafficLight stop')


if __name__ == '__main__':
    tf = TrafficLight()
    tf.running()
