class Base:
    names = "abcdefghijklmnopqrstuvwxyz"
    start_message_1 = "Привет, я здесь чтобы помочь тебе с векторами"
    start_message_2 = "Выбери действие"
    start_actions = [
        "Добавить объект",
        "Операции"
    ]
    add_actions = [
        "Добавить вектор",
        "Добавить точку",
        "Назад"
    ]
    operations = [
        "Найти вектор",
        "Ввести вручную",
        "Помощь",
        "Назад"
    ]
    help = "Длина вектора:          |a|\n" \
           "Сумма векторов:         a+b\n" \
           "Произведение векторов:  a*b"
    error_value = "Неверный формат данных, заполните по образцу:\n" \
                  "ч  ч   ч   и\n" \
                  "ч - число (координата) \n" \
                  "и - имя (при отсутствии задастся автоматически)"


class Point:
    def __init__(self, x, y, z=0, name='a'):
        self.name = name.upper()
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        return f"{self.name} ({str(self.x)};  {str(self.y)}; {str(self.z)})"


class Vector:
    def __init__(self, x, y, z=0, name='a'):
        self.name = name.lower()
        self.x = x
        self.y = y
        self.z = z
        self.len = (x ** 2 + y ** 2 + z ** 2) ** 0.5

    def add_name(self, name: str):
        self.name = name

    def show(self):
        if len(self.name) > 2:
            self.name = self.name[:2]
        if len(self.name) == 2:
            self.name = self.name.upper()
        return f"{self.name} ({str(self.x)};  {str(self.y)}; {str(self.z)})"

    def __add__(self, other):
        vec = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return vec

    def __sub__(self, other):
        vec = Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return vec

    def __mul__(self, other):
        i = self.y * other.z - self.z * other.y
        j = other.x * self.z - self.x * other.z
        k = self.x * other.y - self.y * other.x
        vec = Vector(i, j, k)
        return vec


class Points:
    def __init__(self):
        self.points = {}

    def add_point(self, point: Point):
        self.points[point.name] = point

    def show(self):
        m = "POINTS: \n"
        if len(self.points) == 0:
            return ''
        for point in self.points.keys():
            m += self.points.get(point).show() + "\n"
        return m


class Vectors:
    def __init__(self):
        self.vectors = []

    def add_vec(self, vec: Vector):
        self.vectors.append(vec)

    def find(self, a: Point, b: Point):
        vec = Vector(a.x - b.x, a.y - b.y, a.z - b.z, a.name + b.name)
        self.add_vec(vec)
        return vec

    def show(self):
        m = "VECTORS: \n"
        if len(self.vectors) == 0:
            return ''
        for vec in self.vectors:
            m += vec.show() + "\n"
        return m


def main():
    a = Vector(1, 2, 3)
    b = Vector(3, 2, 1, 'b')
    c = a * b
    c.add_name('c')
    print(c.show())


if __name__ == '__main__':
    main()
