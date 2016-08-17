from math import sin, cos, atan2


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def vect(self, v):
        return Vector3(
            self.y * v.z - self.z * v.y,
            self.z * v.x - self.x * v.z,
            self.x * v.y - self.y * v.x
        )

    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def times(self, s):
        return Vector3(
            self.x * s,
            self.y * s,
            self.z * s
        )

    def sum(self, v):
        return Vector3(self.x + v.x,
                       self.y + v.y,
                       self.z + v.z
                       )

    def diff(self, v):
        return Vector3(self.x - v.x,
                       self.y - v.y,
                       self.z - v.z
                       )

    def magnitude(self):
        return (self.dot(self))**(1/2)

    def normalize(self):
        return self.times(1/self.magnitude())

    def __repr__(self):
        return "<Vector3 ({},{},{})>".format(self.x, self.y, self.z)


class Vector2(Vector3):
    def __init__(self, x, y):
        super(Vector2, self).__init__(x, y, 0)

    def rotate(self, angle):
        return Vector2(self.x*cos(angle) - self.y*sin(angle),
                       self.x*sin(angle) + self.y*cos(angle)
                       )

    def angle(self):
        return atan2(self.x, self.y)
