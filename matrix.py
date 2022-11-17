class Matrix:
    def __init__(self, n, m, name='A'):
        self.matrix = [[0] * n] * m  # n столбцов и m строк
        self.col = n
        self.row = m
        self.name = name

    def read(self):
        for i in range(self.row):
            data = list(map(float, input().split()))[:self.col]
            self.matrix[i] = data

    def show(self):
        res = f'Имя матрицы: {self.name} \n'
        for row in self.matrix:
            res += ', '.join([str(elem) for elem in row]) + '\n'
        return res


mat = Matrix(3, 3, 'SLAVA')
print(mat.show())

c = [[1, 2, 3], [0, 5, 6], [0, 0, 9]]

def linear(some_list):
    if not some_list:
        return some_list
    if type(some_list[0]) is list:
        return linear(some_list[0]) + linear(some_list[1:])
    return some_list[:1] + linear(some_list[1:])


def det(c: list):
    if len(linear(c)) == 1:
        return int(linear([[0]])[0])
    ans = 0
    for i in range(3):
        for j in range(3):