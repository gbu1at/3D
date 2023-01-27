import math

PI = math.pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sqrt = x * x + y * y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def rotate_center(self, center, angle):
        help_p = self - center
        help_p.rotate_angle(angle)
        p = help_p + center
        return p

    def rotate_angle(self, angle):
        x1 = math.cos(angle)
        y1 = math.sin(angle)
        x = self.x
        y = self.y
        self.x = x * x1 - y * y1
        self.y = x1 * y + x * y1

    def __call__(self, *args, **kwargs):
        return self.x, self.y

    def get_dist_to_point(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def set_p1(self, new_p):
        self.p1 = new_p

    def set_p2(self, new_p):
        self.p2 = new_p
