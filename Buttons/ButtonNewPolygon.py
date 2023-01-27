from ROOT.setting import *
import pygame


class ButtonNewPolygon:
    def __init__(self, root_pos=None):
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render("Создать доску", True, GREY)
        self.FOCUS = False
        if root_pos is not None:
            self.x, self.y = root_pos
        else:
            self.x = WIDTH_FOCUS - 2 * self.text.get_width()
            self.y = 2 * self.text.get_height()

    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))
        if self.FOCUS:
            d = 20
            pygame.draw.rect(screen, color=GREY, rect=(
                self.x - d, self.y - d, self.text.get_width() + 2 * d, self.text.get_height() + 2 * d), width=1)

    def is_focus(self, mouse_pos):
        x, y = mouse_pos
        if (self.x <= x <= self.x + self.text.get_width()) and (self.y <= y <= self.y + self.text.get_height()):
            self.FOCUS = True
        else:
            self.FOCUS = False

    def click(self):
        return self.FOCUS
