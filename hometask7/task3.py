#!/usr/bin/env python
# nevl 2021

class Cell:

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        t = self.count - other.count
        if t < 0:
            raise OverflowError
        return Cell(t)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, line_count):
        s = ''
        for _ in range(self.count // line_count):
            s += '*'*line_count + '\n'
        s += '*'*(self.count % line_count) + '\n'
        return s


if __name__ == '__main__':
    cell1 = Cell(31)
    cell2 = Cell(35)
    cell3 = Cell(27)

    for it in [cell1, cell2, cell3]:
        print(it.make_order(9))

    try:
        cell4 = cell1 - cell2
        print(cell4.make_order(9))
    except:
        print('Error')

    try:
        cell5 = cell2 - cell3
        print(cell5.make_order(9))
    except:
        print('Error')
