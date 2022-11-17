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
