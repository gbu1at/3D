import pygame
import math
from ROOT.setting import *

PI = math.pi


class ButtonOK:
    def __init__(self, root_pos=None):
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render("OK", True, GREEN)
        self.FOCUS = False
        if root_pos is not None:
            self.x, self.y = root_pos
        else:
            self.x = WIDTH_FOCUS // 2 - self.text.get_width() // 2
            self.y = HEIGHT_FOCUS - 2 * self.text.get_height()

    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))
        if self.FOCUS:
            d = 10
            pygame.draw.rect(screen, color=WHITE, rect=(
                self.x - d, self.y - d, self.text.get_width() + 2 * d, self.text.get_height() + 2 * d), width=1)

    def is_focus(self, mouse_pos):
        x, y = mouse_pos
        if (self.x <= x <= self.x + self.text.get_width()) and (self.y <= y <= self.y + self.text.get_height()):
            self.FOCUS = True
        else:
            self.FOCUS = False

    def click(self):
        return self.FOCUS


class NewPolygon:
    def __init__(self, rows, cols, size_cell):
        self.rows = rows
        self.cols = cols
        self.size_cell = size_cell
        self.root_coord = (WIDTH_FOCUS // 2 - self.cols * self.size_cell // 2), (
                HEIGHT_FOCUS // 2 - self.rows * self.size_cell // 2 - 20)
        self.board = [[(0, 0, 0) for _ in range(cols)] for _ in range(rows)]
        for row in range(self.rows):
            self.board[row][0] = GREY
            self.board[row][-1] = GREY
        for col in range(self.cols):
            self.board[0][col] = GREY
            self.board[-1][col] = GREY

        self.end_pos = None
        self.start_pos = None

    def draw(self, screen):
        x = self.root_coord[0]
        y = self.root_coord[1]
        size = self.size_cell

        for r in range(self.rows):
            for c in range(self.cols):
                color = self.board[r][c]
                screen.fill(color=color, rect=(x + c * size, y + r * size, size, size))

        pygame.draw.line(screen, color=(255, 255, 255), start_pos=(x, y),
                         end_pos=(x, y + size * self.rows), width=1)
        pygame.draw.line(screen, color=(255, 255, 255), start_pos=(x, y),
                         end_pos=(x + size * self.cols, y), width=1)
        pygame.draw.line(screen, color=(255, 255, 255), start_pos=(x, y + self.rows * size),
                         end_pos=(x + size * self.cols, y + size * self.rows), width=1)
        pygame.draw.line(screen, color=(255, 255, 255), start_pos=(x + self.cols * size, y),
                         end_pos=(x + size * self.cols, y + size * self.rows), width=1)

    def click_response(self, coord_click, color):
        coord_cell = self.get_cell_click(coord_click)
        if coord_cell is None:
            return
        if coord_cell == self.start_pos:
            self.start_pos = None
        if coord_cell == self.end_pos:
            self.end_pos = None
        if color == RED:
            self.clear_cell(self.end_pos)
            self.end_pos = coord_cell
        elif color == GREEN:
            self.clear_cell(self.start_pos)
            self.start_pos = coord_cell
        self.recolor_cell(*coord_cell, color)

    def clear_cell(self, pos):
        if pos is not None:
            x, y = pos
            self.board[x][y] = (0, 0, 0)

    def recolor_cell(self, row, col, color):
        self.board[row][col] = color

    def get_cell_click(self, coord_click):
        c = (coord_click[0] - self.root_coord[0]) // self.size_cell
        r = (coord_click[1] - self.root_coord[1]) // self.size_cell
        if (r < 0) or (r >= self.rows) or (c < 0) or (c >= self.cols):
            return None
        return r, c


class CreateNewPolygon:
    def __init__(self, screen):
        self.screen = screen
        ...

    def start(self):
        game = True
        polygon = NewPolygon(45, 60, 13)
        buttonOK = ButtonOK()
        clock = pygame.time.Clock()
        draw = 0
        color = 0
        while game:
            self.screen.fill((0, 0, 0))
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    draw = True
                    if buttonOK.click():
                        if polygon.end_pos and polygon.start_pos:
                            game = False
                if ev.type == pygame.MOUSEBUTTONUP:
                    draw = False
                if pygame.key.get_pressed()[pygame.K_s]:
                    color = GREEN
                if pygame.key.get_pressed()[pygame.K_e]:
                    color = RED
                if pygame.key.get_pressed()[pygame.K_w]:
                    color = GREY
                if pygame.key.get_pressed()[pygame.K_m]:
                    color = BLUE
                if pygame.key.get_pressed()[pygame.K_c]:
                    color = BLACK
            if draw:
                polygon.click_response(pygame.mouse.get_pos(), color)
            polygon.draw(self.screen)
            buttonOK.draw(self.screen)
            buttonOK.is_focus(pygame.mouse.get_pos())
            pygame.display.update()
            clock.tick(30)

        new_polygon = []
        for line in polygon.board:
            str_line = ""
            for val in line:
                if val == BLACK:
                    str_line += "."
                if val == GREY:
                    str_line += 'W'
                if val == GREEN:
                    str_line += 'S'
                if val == RED:
                    str_line += 'E'
                if val == BLUE:
                    str_line += 'M'
            new_polygon.append(str_line)
        return new_polygon
