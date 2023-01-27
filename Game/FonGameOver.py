from ROOT import setting_commands
from Menu.ButtonMenu import *
from Buttons.ButtonRestart import *
from ROOT.setting_commands import *


class FonGameOver:
    def __init__(self, screen, image="data/fon.png"):
        self.screen = screen
        self.CLOCK = pygame.time.Clock()

        self.button_menu = ButtonMenu(root_pos=(100, 100), ID_PROCESS=ID_SHOW_MENU, text="Меню")
        self.button_restart = ButtonRestart(root_pos=(100, 500), ID_PROCESS=ID_RESTART, text="Начать заново")

        self.buttons = [self.button_menu, self.button_restart]

        self.image = pygame.image.load(image)

        self.FonGameOverProcess = True
        self.ID_NEXT_PROCESS = None

    def start(self):
        while self.FonGameOverProcess:
            self.screen.fill(WHITE)
            self.screen.blit(self.image, (
                WIDTH_FOCUS // 2 - self.image.get_width() // 2, HEIGHT_FOCUS // 2 - self.image.get_height() // 2)
                             )
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    return setting_commands.ID_EXIT
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.click_widgets()
            self.focusing(pygame.mouse.get_pos())
            self.draw_buttons()
            pygame.display.update()
            self.CLOCK.tick(FPS)

        # LoadingAnimation(4, self.screen).start()
        return self.ID_NEXT_PROCESS

    def draw_buttons(self):
        for button in self.buttons:
            button.draw(self.screen)

    def click_widgets(self):
        for button in self.buttons:
            if button.is_click():
                self.FonGameOverProcess = False
                self.ID_NEXT_PROCESS = button.PROCESS

    def focusing(self, mouse_pos):
        for button in self.buttons:
            button.is_focus(mouse_pos)
