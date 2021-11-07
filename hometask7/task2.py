#!/usr/bin/env python
# nevl 2021

from abc import ABC, abstractmethod


class dress(ABC):

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def cloth_rate(self):
        pass


class coat(dress):

    @property
    def cloth_rate(self):
        return self.size / 6.5 + 0.5


class suit(dress):

    @property
    def cloth_rate(self):
        return self.size * 2 + 0.3


if __name__ == '__main__':
    c1 = coat(50)
    print(c1.cloth_rate)

    s1 = suit(1.75)
    print(s1.cloth_rate)

    c2 = coat(54)
    print(c2.cloth_rate)

    s2 = suit(1.85)
    print(s2.cloth_rate)

    print(f'Cloth for all dresses = {s1.cloth_rate + s2.cloth_rate + c1.cloth_rate + c2.cloth_rate}')
