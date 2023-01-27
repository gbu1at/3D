from ROOT.setting import *
import pygame


class MapMenu:
    def __init__(self, root_coord, polygon):
        self.x, self.y = root_coord
        self.polygon = polygon
        self.pix_size = 5
        self.width = self.pix_size * COLS_MAP
        self.height = self.pix_size * ROWS_MAP
        self.FOCUS = False

    def draw(self, screen, dy=0):
        x, y = self.x, self.y + dy
        rect = (x, y, self.width, self.height)
        screen.fill(BLACK, rect)
        for r, line in enumerate(self.polygon.polygon):
            for c, val in enumerate(line):
                color = None
                if val == ".":
                    color = BLACK
                if val == "S":
                    color = GREEN
                if val == "E":
                    color = RED
                if val == "M":
                    color = BLUE
                if val == "W":
                    color = GREY
                screen.fill(color, rect=(x + c * self.pix_size, y + r * self.pix_size, self.pix_size, self.pix_size))

        if self.FOCUS:
            frame_size = 10  # размер рамки
            color = WHITE
            if self.polygon.is_passed:
                color = GREEN
            pygame.draw.rect(surface=screen, color=color, rect=(
                x - frame_size, y - frame_size, self.width + 2 * frame_size, self.height + 2 * frame_size), width=2)

    def is_focus(self, mouse_pos):
        x, y = mouse_pos
        if (self.x < x < self.x + self.width) and (self.y < y < self.y + self.height):
            self.FOCUS = True
        else:
            self.FOCUS = False

    def save(self):
        self.polygon.save()

    def map_passed(self):
        self.polygon.is_passed = True
