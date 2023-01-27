from ROOT import setting
from ROOT.setting import *
from math import *
import pygame


def is_correct_move_player(x, y):
    if (x // WIDTH_PIX, y // WIDTH_PIX) == setting.POS_END:
        setting.CHANGE_END_POS = True
        return True
    if (x // WIDTH_PIX, y // WIDTH_PIX, ID_WALL) in setting.OBJECTS:
        return False
    if (x // WIDTH_PIX, y // WIDTH_PIX, ID_MONSTER) in setting.OBJECTS:
        setting.GAME = False
        setting.KILL_PLAYER = True
        return True
    return True


def get_length_ray_object(start_coord, angle, name_objects):
    cos_angle = cos(angle)
    sin_angle = sin(angle)
    x, y = start_coord
    min_length = setting.DISTANCE
    for name_object in name_objects:
        for length in range(1, min_length, 3):
            dx, dy = length * cos_angle, length * sin_angle
            if ((x + dx) // WIDTH_PIX, (y + dy) // WIDTH_PIX, name_object) in setting.OBJECTS:
                min_length = min(length, min_length)
                break

    return min_length


def get_height_from_length(length):
    return HEIGHT_FOCUS * MIN_DISTANCE / length


def is_wall_coord(x, y):
    if x < 0 or x >= setting.COLS:
        return True
    if y < 0 or y >= setting.ROWS:
        return True
    return (x, y, ID_WALL) in setting.OBJECTS


def is_free_cell(x, y):
    if (x, y, ID_WALL) in setting.OBJECTS:
        return False
    if (x, y, ID_MONSTER) in setting.OBJECTS:
        return False
    return True


def is_exit(self):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            exit()
