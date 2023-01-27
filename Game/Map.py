from Game.Board import *
from ROOT.setting import *
import pygame


class Map:
    def __init__(self):
        self.width = WIDTH_PIX_MAP * COLS_MAP
        self.height = WIDTH_PIX_MAP * ROWS_MAP
        self.x = WIDTH_FOCUS - self.width - 20
        self.y = 20
        self.is_BIG = False
        self.FOCUS = False
        self.SHOW = False

    def draw(self, screen, player_pos):
        screen.fill(BLACK,
                    (self.x, self.y, self.width, self.height))
        for cell in setting.OBJECTS:
            x, y, name_obj = cell
            color = COLOR_MAP[name_obj]
            screen.fill(color, (
                self.x + x * setting.WIDTH_PIX_MAP, self.y + y * setting.WIDTH_PIX_MAP, setting.WIDTH_PIX_MAP,
                setting.WIDTH_PIX_MAP))

        x_player, y_player = player_pos
        x_player //= WIDTH_PIX
        y_player //= WIDTH_PIX

        screen.fill(GREEN, (
            self.x + x_player * setting.WIDTH_PIX_MAP, self.y + y_player * setting.WIDTH_PIX_MAP, setting.WIDTH_PIX_MAP,
            setting.WIDTH_PIX_MAP))

        frame_size = 10  # размер рамки
        if self.FOCUS:
            pygame.draw.rect(surface=screen, color=WHITE,
                             rect=(self.x - frame_size, self.y - frame_size, self.width + 2 * frame_size,
                                   self.height + 2 * frame_size), width=2)

    def is_focus(self, mouse_pos):
        x, y = mouse_pos
        if (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height):
            self.FOCUS = True
            return True
        else:
            self.FOCUS = False
            return False

    def make_small(self):
        self.__init__()
        self.SHOW = True
        setting.WIDTH_PIX_MAP = 5

    def make_big(self):
        self.is_BIG = True
        D = 100
        coeff = (HEIGHT_FOCUS - D) // self.height
        self.height *= coeff
        self.width *= coeff
        setting.WIDTH_PIX_MAP *= coeff
        self.x = WIDTH_FOCUS // 2 - self.width // 2
        self.y = HEIGHT_FOCUS // 2 - self.height // 2

    def click(self, *args, **kwargs):
        if self.FOCUS and self.SHOW:
            if self.is_BIG:
                self.make_small()
            else:
                self.make_big()
        return 0

    def pinch(self, *args, **kwargs):
        ...

    def decompression_mouse(self, *args, **kwargs):
        ...