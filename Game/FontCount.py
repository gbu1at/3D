import pygame


class FontCount:
    def __init__(self, count, max_count, pos):
        self.x, self.y = pos

        self.count = count
        self.max_count = max_count

        self.color = (100, 100, 130)

        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render(f"{count} / {max_count}", True, self.count)

        self.width = self.text.get_width()
        self.height = self.text.get_height()

        self.SHOW = True
        self.FOCUS = False

    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))

    def set_count(self):
        self.count += 1
        self.text = self.font.render(f"{self.count} / {self.max_count}", True, self.count)

    def click(self, *args, **kwargs):
        return 0

    def is_focus(self, mouse_pos):
        x, y = mouse_pos
        if (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height):
            self.FOCUS = True
            return True
        else:
            self.FOCUS = False
            return False

    def pinch(self, *args, **kwargs):
        ...

    def decompression_mouse(self, *args, **kwargs):
        ...
