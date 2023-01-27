from ROOT.functions import is_correct_move_player
from Game.camera import Camera
import math
import pygame
from ROOT.setting import *
import ROOT.setting


class Player:
    def __init__(self, pos):
        self.x, self.y = pos
        self.focus_angle = 0

        self.camera = Camera(self.x, self.y, self.focus_angle)
        self.FORWARD = 3274875
        self.BEHIND = 756483

        self.CAMERA_SIDE = self.FORWARD

    def movement(self):
        cos_angle = math.cos(self.focus_angle)
        sin_angle = math.sin(self.focus_angle)
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            dx = ROOT.setting.SPEED_PLAYER * cos_angle
            dy = ROOT.setting.SPEED_PLAYER * sin_angle

        if key[pygame.K_s]:
            dx = -ROOT.setting.SPEED_PLAYER * cos_angle
            dy = -ROOT.setting.SPEED_PLAYER * sin_angle

        if key[pygame.K_a]:
            dx = ROOT.setting.SPEED_PLAYER * sin_angle
            dy = -ROOT.setting.SPEED_PLAYER * cos_angle

        if key[pygame.K_d]:
            dx = -ROOT.setting.SPEED_PLAYER * sin_angle
            dy = ROOT.setting.SPEED_PLAYER * cos_angle

        if key[pygame.K_LEFT]:
            self.focus_angle -= 0.08

        if key[pygame.K_RIGHT]:
            self.focus_angle += 0.08

        self.move_dxy(dx, dy)
        if self.CAMERA_SIDE == self.FORWARD:
            self.camera = Camera(self.x, self.y, self.focus_angle)
        if self.CAMERA_SIDE == self.BEHIND:
            self.camera = Camera(self.x, self.y, pi + self.focus_angle)

    def move_dxy(self, dx, dy):
        if is_correct_move_player(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    def get_pos(self):
        return self.x, self.y

    def set_camera(self):
        if self.CAMERA_SIDE == self.FORWARD:
            self.CAMERA_SIDE = self.BEHIND
        else:
            self.CAMERA_SIDE = self.FORWARD

    def draw_player_and_his_focus(self, screen):
        font = pygame.font.Font(None, 45)
        if self.CAMERA_SIDE == self.FORWARD:
            text = font.render("FORWARD", True, BLUE)
        if self.CAMERA_SIDE == self.BEHIND:
            text = font.render("BEHIND", True, BLUE)
        self.camera.draw_rays(screen)
        screen.blit(text, (WIDTH_FOCUS // 2 - text.get_width() // 2, 20))
