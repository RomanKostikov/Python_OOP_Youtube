class Point:
    """Класс для представления координат точек на плоскости."""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        self.__x = x
        self.__y = y

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())
