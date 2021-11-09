#!/usr/bin/env python
# nevl 2021

class MyComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return MyComplex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return MyComplex(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)

    def __str__(self):
        return '({}{}{}j)'.format(self.a, '+' if self.b >= 0 else '', self.b)


if __name__ == '__main__':
    c1 = MyComplex(2, 3)
    c2 = MyComplex(-1, 0)
    c3 = c1 + c2
    c4 = c1 * c2

    for it in [c1, c2, c3, c4]:
        print(it)
