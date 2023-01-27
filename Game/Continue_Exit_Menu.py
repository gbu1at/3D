from Buttons.ButtonContinue import *
from Buttons.ButtonExit import *
from ROOT.setting_commands import *
from Game.Slider import *
from ROOT.setting import *


class ContinueExitMenu:
    def __init__(self, root_pos):
        self.x, self.y = root_pos
        self.width = 800
        self.height = 120
        self.cont = ButtonContinue((self.x + 10, self.y + 10), ID_PROCESS=0, text="Продолжить", color_text=GREY)
        self.exit = ButtonExit((self.x + self.width - 210, self.y + 10), ID_PROCESS=ID_SHOW_MENU, text="Выйти",
                               color_text=GREY)

        self.sliders = SliderGroup()

        Slider(root_pos=(WIDTH_FOCUS // 2, 100), length=100, text="Яркость",
               slider_group=self.sliders, ID_PARAMETR=ID_BRIGHTNESS)
        Slider(root_pos=(WIDTH_FOCUS // 2, 200), length=100, text="Дистанция",
               slider_group=self.sliders, ID_PARAMETR=ID_DISTANCE)

        self.SHOW = False
        self.FOCUS = False

    def draw(self, screen):
        self.cont.draw(screen)
        self.exit.draw(screen)
        self.sliders.draw(screen)

    def is_focus(self, mouse_pos):
        self.cont.is_focus(mouse_pos)
        self.exit.is_focus(mouse_pos)
        self.sliders.is_focus(mouse_pos)
        self.FOCUS = self.cont.FOCUS or self.exit.FOCUS or self.sliders.FOCUS

    def click(self):
        if self.cont.is_click():
            self.SHOW = False
            self.FOCUS = False
            setting.STOP_GAME = False
            return self.cont.PROCESS
        if self.exit.is_click():
            self.SHOW = False
            self.FOCUS = False
            setting.STOP_GAME = False
            return self.exit.PROCESS
        self.sliders.is_click()
        return 0

    def pinch(self, mouse_pos):
        self.sliders.move(mouse_pos)

    def decompression_mouse(self):
        self.sliders.decompression_mouse()
