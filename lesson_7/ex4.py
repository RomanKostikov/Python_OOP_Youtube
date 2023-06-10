class Point:
    MIN_COORD = 100
    MAX_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("доступ запрещен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            # object.__setattr__(self, key, value)
            self.__dict__[key] = value

    # def __getattr__(self, item):
    #     print("__getattr__: " + item)
    def __getattr__(self, item):  # для чего нужен(пример)
        return False


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.yy)
print(pt1.y)
