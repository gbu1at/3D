from Geometry.Geometry import Point
from ROOT.functions import *

from ROOT.setting import *


class Slider:
    def __init__(self, root_pos, length, slider_group, ID_PARAMETR, text="None", radius=10):
        self.ID_PARAMETR = ID_PARAMETR
        slider_group.append(self)
        self.length = length
        self.radius = radius
        self.x, self.y = root_pos
        self.CLOCK = pygame.time.Clock()
        self.slider_center = root_pos[0] + radius // 2, root_pos[1] + radius // 2
        self.FOCUS = False
        self.SHOW = False
        self.MOVE = False
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render(text, True, RED)

    def is_focus(self, mouse_pos):
        x, y = mouse_pos
        if Point(x, y).get_dist_to_point(Point(*self.slider_center)) < self.radius:
            self.FOCUS = True
            return True
        else:
            self.FOCUS = False
            self.MOVE = False
            return False

    def draw(self, screen):
        pygame.draw.rect(screen, border_radius=5, rect=(
            self.x, self.y, self.length, self.radius), color=(150, 150, 150))
        pygame.draw.circle(screen, color=WHITE, center=self.slider_center, radius=self.radius)
        screen.blit(self.text,
                    (self.x - self.text.get_width() - 30, self.y + self.radius // 2 - self.text.get_height() // 2))

    def is_click(self):
        if self.FOCUS:
            self.MOVE = True
            return True
        return False

    def move(self, mouse_pos):
        if self.MOVE and self.FOCUS:
            x, y = self.slider_center
            x = mouse_pos[0]
            if x < self.x:
                x = self.x
            if x > self.x + self.length:
                x = self.x + self.length
            self.slider_center = (x, y)

        if self.ID_PARAMETR == ID_BRIGHTNESS:
            setting.BRIGHTNESS = -(self.slider_center[0] - self.x) * 0.000001 + 0.0001
        if self.ID_PARAMETR == ID_DISTANCE:
            setting.DISTANCE = 4 * (self.slider_center[0] - self.x) + 300

    def decompression_mouse(self):
        self.MOVE = False


class SliderGroup:
    def __init__(self):
        self.sliders = []
        self.FOCUS = False

    def append(self, slider):
        self.sliders.append(slider)

    def move(self, mouse_pos):
        for slider in self.sliders:
            if slider.FOCUS:
                slider.move(mouse_pos)

    def decompression_mouse(self):
        for slider in self.sliders:
            slider.decompression_mouse()

    def is_click(self):
        for slider in self.sliders:
            slider.is_click()

    def is_focus(self, mouse_pos):
        for num, slider in enumerate(self.sliders):
            slider.is_focus(mouse_pos)
            self.FOCUS = self.FOCUS or slider.is_focus(mouse_pos)

    def draw(self, screen):
        for slider in self.sliders:
            slider.draw(screen)
