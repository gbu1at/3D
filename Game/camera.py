from ROOT.functions import *
import pygame
import math


class Camera:
    def __init__(self, x, y, root_angle, range_angle=RANGE_ANGLE):
        self.x = x
        self.y = y
        self.root_angle = root_angle
        self.delta_angle = range_angle / COUNT_RAYS
        self.list_visible_rays = []
        self.ray_range()

    def ray_range(self):
        angle = self.root_angle - (COUNT_RAYS * self.delta_angle / 2)
        for number_ray in range(COUNT_RAYS):
            cos_angle = math.cos(angle)
            sin_angle = math.sin(angle)

            start_pos = self.x, self.y

            length_to_object = get_length_ray_object(start_pos, angle, names_ID)
            length_to_wall = get_length_ray_object(start_pos, angle, [ID_WALL])

            end_pos_to_object = self.x + cos_angle * length_to_object, self.y + sin_angle * length_to_object
            end_pos_to_wall = self.x + cos_angle * length_to_wall, self.y + sin_angle * length_to_wall

            coeff_fish_eye = math.cos(self.root_angle - angle)

            ray = Ray(start_pos, end_pos_to_object, number_ray, coeff_fish_eye, end_pos_to_wall)

            self.list_visible_rays.append(ray)
            angle += self.delta_angle

    def draw_rays(self, screen):
        for ray in self.list_visible_rays:
            ray.draw(screen)


class Ray:
    def __init__(self, start_pos, end_pos_to_object, number, coeff_fish_eye, end_pos_to_wall):
        self.start_pos = start_pos
        self.end_pos_to_object = end_pos_to_object
        self.end_pos_to_wall = end_pos_to_wall
        self.number = number
        self.coeff_fish_eye = coeff_fish_eye

    def draw(self, screen):
        self.draw_board_wall(screen, self.get_rect_to_object(self.get_length_to_wall))
        self.draw_monster(screen, self.get_rect_to_object(self.get_length_to_object))
        self.draw_finish(screen, self.get_rect_to_object(self.get_length_to_object))

    def get_rect_to_object(self, func_get_length):
        delta_width = WIDTH_FOCUS / COUNT_RAYS
        length = func_get_length()
        height = get_height_from_length(length) / self.coeff_fish_eye
        x_start = WIDTH_FOCUS / COUNT_RAYS * self.number
        y_start = HEIGHT_FOCUS // 2 - height // 2
        return x_start, y_start, delta_width, height

    def draw_board_wall(self, screen, rect):
        length = self.get_length_to_wall()
        c = 255 // max(1, int(length * length * setting.BRIGHTNESS))
        color = (c // 2, c // 2, c // 2)
        x_e, y_e = self.end_pos_to_wall

        if (x_e // WIDTH_PIX, y_e // WIDTH_PIX, ID_WALL) in setting.OBJECTS:
            pygame.draw.rect(surface=screen, color=color, rect=rect)

    def draw_finish(self, screen, rect):
        length = self.get_length_to_object()
        x_start, y_start, delta_width, height = rect
        c = 255 // max(1, int(length * length * setting.BRIGHTNESS))
        color = (c, c // 2, c // 2)
        x_e, y_e = self.end_pos_to_object
        if (x_e // WIDTH_PIX, y_e // WIDTH_PIX) == setting.POS_END:
            pygame.draw.rect(surface=screen, color=color,
                             rect=(x_start, y_start, delta_width // 2, height))

    def draw_monster(self, screen, rect):
        x_start, y_start, delta_width, height = rect
        length = self.get_length_to_object()
        if length > self.get_length_to_wall():
            return
        c = 255 // max(1, int(length * length * setting.BRIGHTNESS))
        color = (c // 2, c // 2, c)
        x_e, y_e = self.end_pos_to_object

        if (x_e // WIDTH_PIX, y_e // WIDTH_PIX, ID_MONSTER) in setting.OBJECTS:
            pygame.draw.rect(surface=screen, color=color, rect=(x_start, y_start, delta_width, height))

    def get_length_to_object(self):
        x_s, y_s = self.start_pos
        x_e, y_e = self.end_pos_to_object
        return math.sqrt((x_s - x_e) ** 2 + (y_s - y_e) ** 2)

    def get_length_to_wall(self):
        x_s, y_s = self.start_pos
        x_e, y_e = self.end_pos_to_wall
        return math.sqrt((x_s - x_e) ** 2 + (y_s - y_e) ** 2)
