import pygame

pygame.init()
from ROOT.setting import *
import ROOT.setting
from random import randint


class Effects:
    def __init__(self, timer, random_time, text):
        self.clock = pygame.time.Clock()
        self.random_time = random_time
        self.timer = timer
        self.EFFECT = False
        self.TIME_START = None
        self.TIME_END = self.timer
        self.font = pygame.font.Font(None, 20)
        self.text = self.font.render(text, True, RED)

    def random(self):
        a = randint(0, FPS * self.random_time)
        if a == 1:
            self.EFFECT = True

    def effect(self, *args, **kwargs):
        ...

    def draw(self, canvas):
        canvas.blit(self.text, (WIDTH_FOCUS // 2 - self.text.get_width() // 2, HEIGHT_FOCUS - 200))


class StunEffect(Effects):
    def __init__(self, timer=TIME_STAN_EFFECT, random_time=RANDOM_TIME_STAN_EFFECT, text='stan'):
        super().__init__(timer, random_time, text)
        self.surf = pygame.Surface((WIDTH_FOCUS, HEIGHT_FOCUS))
        self.surf.fill(WHITE)

    def effect(self, screen):
        if self.TIME_START is None:
            self.TIME_START = 0
        if self.TIME_START > self.TIME_END:
            self.EFFECT = False
            self.TIME_START = None
            return
        self.TIME_START += 1 / FPS
        self.surf.set_alpha(int((self.timer - self.TIME_START) * 150))
        self.draw(self.surf)
        screen.blit(self.surf, (0, 0))


class SpeedEffect(Effects):
    def __init__(self, timer=TIME_SPEED_PLAYER_EFFECT, random_time=RANDOM_TIME_SPEED_PLAYER_EFFECT, text='speed'):
        super().__init__(timer, random_time, text)

    def effect(self):
        if self.TIME_START is None:
            self.TIME_START = 0
        if self.TIME_START > self.TIME_END:
            self.EFFECT = False
            self.TIME_START = None
            ROOT.setting.SPEED_PLAYER = 2
            return
        ROOT.setting.SPEED_PLAYER = 4
        self.TIME_START += 1 / FPS

    def no_effect(self):
        ROOT.setting.SPEED_PLAYER = 2


stun_effect = StunEffect()
speed_effect = SpeedEffect()


def func_stun_effect(screen):
    if stun_effect.EFFECT:
        stun_effect.effect(screen)
    else:
        stun_effect.random()


def func_speed_effect(screen):
    if speed_effect.EFFECT:
        speed_effect.effect()
        speed_effect.draw(screen)
    else:
        speed_effect.no_effect()
        speed_effect.random()


def func_effect(screen):
    func_stun_effect(screen)
    func_speed_effect(screen)
