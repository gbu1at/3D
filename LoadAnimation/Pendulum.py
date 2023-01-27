from Geometry.Geometry import *
from ROOT.setting import *
import pygame

EPS = 3


class Pendulum:
    def __init__(self):
        self.center = Point(WIDTH_FOCUS // 2, HEIGHT_FOCUS // 2)
        self.c1 = CircleAnimation(self.center + Point(100, 0), 10, 2)
        self.c2 = CircleAnimation(self.center - Point(100, 0), 10, 2)
        self.circles = [self.c1, self.c2]

    def draw(self, screen):
        self.c1.draw(screen)
        self.c2.draw(screen)

    def move(self):
        for c in self.circles:
            if c.get_y() - EPS <= HEIGHT_FOCUS // 2 <= c.get_y() + EPS:
                c.speed = 2

            c.speed += c.a
            c.rotate_angle(self.center)


class CircleAnimation:
    def __init__(self, center, radius, spped):
        self.center = center
        self.radius = radius
        self.speed = spped
        self.a = 0.2

    def draw(self, screen):
        pygame.draw.circle(screen, color=WHITE, center=self.center(), radius=10)

    def rotate_angle(self, center):
        new_center = self.center.rotate_center(center, self.speed / 180)
        self.center = new_center

    def get_y(self):
        return self.center.y
