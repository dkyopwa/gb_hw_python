#!/usr/bin/env python
# nevl 2021

class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Drawing start')


class Pen(Stationery):
    def __init__(self, title='Pen'):
        super().__init__(title)

    def draw(self):
        print(f'Drawing super puper pen: {self.title}')


class Pencil(Stationery):
    def __init__(self, title='Pencil'):
        super().__init__(title)

    def draw(self):
        print(f'Pencil is a very important thing: {self.title}')


class Handle(Stationery):
    def __init__(self, title='Handle'):
        super().__init__(title)

    def draw(self):
        print(f'Handle is permanent marker: {self.title}')


if __name__ == '__main__':
    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()
