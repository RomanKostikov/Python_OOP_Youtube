class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left


pt1 = Point(1, 2)
pt2 = Point(10, 20)
pt1.set_bound(-100)
print(pt1.__dict__)
print(Point.__dict__)
