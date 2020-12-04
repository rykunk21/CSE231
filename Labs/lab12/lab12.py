import math

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.magnitude = None

    def __str__(self):
        return 'x = {:.2f}, y = {:.2f}'.format(self.x, self.y)

    def __repr__(self):
        return 'x = {:.2f}, y = {:.2f}'.format(self.x, self.y)

    def __add__(self, other):
        if type(other) == Vector:
            return Vector((self.x + other.x), (self.y + other.y))
        else:
            raise TypeError

    def __sub__(self, other):
        if type(other) == Vector:
            return Vector((self.x - other.x), (self.y - other.y))
        else:
            raise TypeError

    def __mul__(self, other):
        if type(other) == Vector:
            return Vector((self.x * other.x), (self.y * other.y))
        else:
            return Vector((self.x * other), (self.y * other))

    def __rmul__(self, other):
        if type(other) == Vector:
            return Vector((self.x * other.x), (self.y * other.y))
        elif type(other) == float:
            return Vector((self.x * other),(self.y * other))
        else:
            raise TypeError

    def __eq__(self, other):
        if type(other) == Vector:
            return self.x == other.x and self.y == other.y
        else:
            raise TypeError

    def magnitude(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def unit(self):
        self.magnitude = 1 / self.magnitude()
        if self.magnitude == 0:
            raise ValueError("Cannot convert zero vector to a unit vector")
        else:
            self.x *= self.magnitude
            self.y *= self.magnitude



a = Vector(2, 4)

print(a)
