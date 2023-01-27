from Game.Map import *
from Game.player import Player
from Game.FonGameOver import *
from Game.Continue_Exit_Menu import *
from Game.FontCount import FontCount
from threading import Thread
from LoadAnimation.LoadingAnimation import *
from Game.StunEffect import func_effect
import pygame

pygame.init()


class Game:
    def __init__(self, polygon):
        self.screen = pygame.display.set_mode((WIDTH_FOCUS, HEIGHT_FOCUS))
        self.CLOCK = pygame.time.Clock()
        self.board = Board(polygon)

        self.map = Map()
        self.continue_exit_menu = ContinueExitMenu((225, HEIGHT_FOCUS - 200))
        self.font_count = FontCount(count=0, max_count=setting.COUNT_POINT, pos=(50, 50))

        self.widgets = [self.map, self.continue_exit_menu, self.font_count]

        self.player = Player((self.board.x_s * WIDTH_PIX, self.board.y_s * WIDTH_PIX))
        self.CLOCK_MONSTER = 0

        self.ID_NEXT_PROCESS = 0

        self.MOUSE_PINCH = False

    def setting(self):
        bfs.init()
        setting.GAME_INIT = True

    def draw(self):
        self.player.draw_player_and_his_focus(self.screen)

    def moving_monster(self):
        if self.CLOCK_MONSTER < 2000:
            self.CLOCK_MONSTER += 3500 / FPS
            return

        self.CLOCK_MONSTER = 0
        for monster in setting.MONSTER_map:
            x, y = monster.get_pos()
            x_player, y_player = self.player.get_pos()

            x_player //= setting.WIDTH_PIX
            y_player //= setting.WIDTH_PIX

            monster.move_to_player((int(x_player), int(y_player)))

            setting.OBJECTS.remove((x, y, ID_MONSTER))
            setting.OBJECTS.add((monster.x, monster.y, ID_MONSTER))

            if (x_player, y_player) == monster.get_pos():
                setting.GAME = False

    def start(self):
        setting.GAME_INIT = False
        setting.KILL_PLAYER = False
        setting.WIN_PLAYER = False
        t2 = Thread(target=lambda: LoadingAnimation(8, self.screen))
        t2.start()
        t1 = Thread(target=self.setting())
        t1.start()

        setting.STOP_GAME = False
        setting.GAME = True

        while setting.GAME and self.ID_NEXT_PROCESS == 0:
            self.screen.fill(BLACK)
            H = 10 * 300 / setting.DISTANCE
            self.screen.fill((100, 100, 140), (0, 0, WIDTH_FOCUS, HEIGHT_FOCUS // 2 - H))
            self.screen.fill((10, 70, 10), (0, HEIGHT_FOCUS // 2 + H, WIDTH_FOCUS, HEIGHT_FOCUS // 2))

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    return ID_EXIT

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.MOUSE_PINCH = True
                    self.click_widgets()

                if ev.type == pygame.MOUSEBUTTONUP:
                    self.MOUSE_PINCH = False
                    self.decompression_mouse()

                if ev.type == pygame.KEYDOWN:
                    self.click_on_keyboard()

            if self.MOUSE_PINCH:
                self.pinch_widget(pygame.mouse.get_pos())

            if setting.CHANGE_END_POS:
                self.font_count.set_count()
                if setting.COUNT_POINT == self.font_count.count:
                    setting.GAME = False
                    setting.WIN_PLAYER = True
                self.board.change_pos_end()
                setting.CHANGE_END_POS = False

            self.focusing_on_widgets()

            self.draw()

            self.showing_widgets()

            if not setting.STOP_GAME:
                self.moving_objects()
                self.continue_exit_menu.SHOW = False
                func_effect(self.screen)

            else:
                self.continue_exit_menu.SHOW = True

            pygame.display.update()
            self.CLOCK.tick(FPS)
            # print("\r", self.CLOCK.get_fps(), end="")

        if setting.KILL_PLAYER:
            image = "data/fon_death.png"
            fon_game_over = FonGameOver(self.screen, image)
            return fon_game_over.start()
        return ID_SHOW_MENU

    def focusing_on_widgets(self):
        mouse_pos = pygame.mouse.get_pos()
        for widget in self.widgets:
            widget.is_focus(mouse_pos)

    def showing_widgets(self):
        if self.map.SHOW:
            self.map.draw(self.screen, self.player.get_pos())
        if self.continue_exit_menu.SHOW:
            self.continue_exit_menu.draw(self.screen)
        if self.font_count.SHOW:
            self.font_count.draw(self.screen)

    def moving_objects(self):
        self.moving_monster()
        self.player.movement()

    def click_widgets(self):
        for widget in self.widgets:
            if widget.FOCUS:
                self.ID_NEXT_PROCESS = widget.click()

    def pinch_widget(self, mouse_pos):
        for widget in self.widgets:
            if widget.FOCUS:
                widget.pinch(mouse_pos)

    def click_on_keyboard(self):
        key = pygame.key.get_pressed()
        if not setting.STOP_GAME:
            if key[pygame.K_p]:
                self.map.SHOW = not self.map.SHOW
        if key[pygame.K_RETURN]:
            setting.STOP_GAME = not setting.STOP_GAME
            if setting.STOP_GAME:
                self.map.make_small()

        if key[pygame.K_l]:
            self.map.FOCUS = True
            self.map.click()

        if key[pygame.K_m]:
            self.player.set_camera()

    def decompression_mouse(self):
        for widget in self.widgets:
            widget.decompression_mouse()
