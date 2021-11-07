#!/usr/bin/env python
# nevl 2021

class Matrix:

    def __init__(self, data):
        if not type(data) is list or not type(data[0]) is list:
            print('Not a matrix. Try again')
            return

        self.matrix_data = data

    def __str__(self):
        result = ''
        for iter in self.matrix_data:
            s = '['
            for item in iter:
                s += f'{item}\t'
            result += f'{s}]\n'
        return result

    def __add__(self, other):
        data = list()
        # check shape
        if len(self.matrix_data) != len(other.matrix_data) or len(self.matrix_data[0]) != len(other.matrix_data[0]):
            return None

        # calculate
        for i in range(len(self.matrix_data)):
            data.append(list())
            for j in range(len(self.matrix_data[0])):
                data[i].append(self.matrix_data[i][j] + other.matrix_data[i][j])

        return Matrix(data)


if __name__ == '__main__':
    mart1 = Matrix([[1, 2, 3], [3, 4, 5]])
    print(mart1)

    mart2 = Matrix([[1.1, 2.2, 3.3], [3.3, 4.4, 5.5]])
    print(mart2)

    print(mart1 + mart2)
