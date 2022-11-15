""" Модуль векторов """


class Point:
    """ Класс точки """

    def __init__(self, x: int, y: int, z: int = 0, name: str = 'a'):
        """
        :param x: Координата x
        :param y: Координата y
        :param z: Координата z
        :param name: Название точки
        """
        self.name = name.upper()
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        """ Метод отображения точки """
        return f"{self.name} ({str(self.x)};  {str(self.y)}; {str(self.z)})"


class Vector:
    """ Класс вектора """

    def __init__(self, x: int, y: int, z: int = 0, name: str = 'a'):
        """
        :param x: Координата x
        :param y: Координата y
        :param z: Координата z
        :param name: Название вектора
        """
        self.name = name.lower()
        self.x = x
        self.y = y
        self.z = z
        self.len = (x ** 2 + y ** 2 + z ** 2) ** 0.5  # Длина вектора

    def change_name(self, name: str):
        """ Метод смены названия вектора """
        self.name = name

    def show(self):
        """ Метод отображения вектора """
        if len(self.name) > 2:
            self.name = self.name[:2]
        if len(self.name) == 2:
            self.name = self.name.upper()
        return f"{self.name} ({str(self.x)};  {str(self.y)}; {str(self.z)})"

    def __add__(self, other):
        """ Переопределение оператора сложения векторов """
        vec = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return vec

    def __sub__(self, other):
        """ Переопределение оператора вычитания векторов """
        vec = Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return vec

    def __mul__(self, other):
        """ Переопределение оператора векторного умножения векторов """
        i = self.y * other.z - self.z * other.y
        j = other.x * self.z - self.x * other.z
        k = self.x * other.y - self.y * other.x
        vec = Vector(i, j, k)
        return vec


class Points:
    """ Класс точек """

    def __init__(self):
        self.points = {}  # Словарь(ключ - имя точки, значение - Точка)

    def add_point(self, point: Point):
        """ Метод добавления точки в словарь """
        self.points[point.name] = point

    def show(self):
        """ Метод отображения точек """
        m = "ТОЧКИ: \n"
        if len(self.points) == 0:
            return ''
        for point in self.points.keys():
            m += self.points.get(point).show() + "\n"
        return m


class Vectors:
    def __init__(self):
        self.vectors = {}  # Словарь(ключ - имя вектора, значение - Вектор)

    def add_vec(self, vec: Vector):
        """ Метод добавления вектора в словарь """
        self.vectors[vec.name] = vec

    def find(self, a: Point, b: Point):
        """ Метод нахождения вектора по двум точкам """
        vec = Vector(a.x - b.x, a.y - b.y, a.z - b.z, a.name + b.name)
        self.add_vec(vec)
        return vec

    def show(self):
        """ Метод отображения векторов """
        m = "ВЕКТОРЫ: \n"
        if len(self.vectors) == 0:
            return ''
        for vec in self.vectors:
            m += vec.show() + "\n"
        return m


def main():
    """ TESTS """
    a = Vector(1, 2, 3)
    b = Vector(3, 2, 1, 'b')
    s = 'a+b'
    print()


if __name__ == '__main__':
    main()