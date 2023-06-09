class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


v = Vector(1, 2)
res = v.get_coords()
print(res)
