from ROOT.setting import *
import pygame


class ButtonNavigation:
    def __init__(self, root_pos, ID_PROCESS, text="Text", color_text=BLUE):
        self.x, self.y = root_pos
        self.FOCUS = False
        self.PROCESS = ID_PROCESS

        self.color_text = color_text

        self.font = pygame.font.Font(None, 35)
        self.text = self.font.render(text, True, self.color_text)

        self.width = self.text.get_width()
        self.height = self.text.get_height()

    def draw(self, screen, dy=0):
        screen.blit(self.text, (self.x, self.y + dy))

        if self.FOCUS:
            frame_size = 20  # размер рамки
            pygame.draw.rect(surface=screen, color=self.color_text, rect=(
                self.x - frame_size, self.y - frame_size + dy, self.width + 2 * frame_size,
                self.height + 2 * frame_size),
                             width=2)

    def is_focus(self, mouse_pos, dy=0):
        x, y = mouse_pos
        if (self.x <= x <= self.x + self.width) and (self.y - dy <= y <= self.y + self.height - dy):
            self.FOCUS = True
        else:
            self.FOCUS = False

    def is_click(self):
        return self.FOCUS
