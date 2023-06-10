class Point:
    """Класс для представления координат точек на плоскости."""

    def __init__(self, x, y):
        self._x = x
        self._y = y


pt = Point(1, 2)
print(pt._x, pt._y)
