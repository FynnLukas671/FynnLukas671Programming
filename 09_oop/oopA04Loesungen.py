class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}/{self.y})"

p1 = Point(1, 1)
p2 = Point(2, 1)
p3 = Point(1, 1)

print(p1, p1.__eq__(p2), p1.__eq__(p3))

