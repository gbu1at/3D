from Buttons.ButtonNavigation import *
from ROOT.setting_commands import *
import pygame


class ButtonInstruction(ButtonNavigation):
    ...


class Instruction:
    def __init__(self):
        self.button_exit = ButtonNavigation(root_pos=(WIDTH_FOCUS // 2 - 50, HEIGHT_FOCUS + 400), text="выход",
                                            ID_PROCESS=0, color_text=GREY)
        self.text = """
                        Правила игры очень просты:\n
                            1) Управление у игры стандартное (asdw)\n
                            2) Необходимо собрать 7 красных точек за игру\n
                            3) нужно убегать от синих квадратов\n
                            4) Клавиша m меняет обзор\n
                            5) enter - останавливает игру\n
                            6) Нажмите 'p', чтобы открыть карту. Клавиша l увеличивает изображение карты\n
                            7) Во время игры может наложиться эффект stan\n
                            8) Вы можете сами создавать и удалять свои карты\n
                                5.1 Чтобы создать карут нажмите кнопку 'Создать карту'\n
                                5.2 Объекты на карту ставятся с зажатой мышью\n
                                5.3 Прежде чем его поставить, нажмите на кнопку соответствующую объекту\n
                                5.4 s - стартовая вершина, w - стена, m - враг, e - конечная вершина, c - стереть объект\n
                            9) Чтобы удалить карту, сфокусируйтесь на ней и нажмите del\n
                            10) Вы не сможете удалить начальные карты\n
                            11) Если вы смогли пройти карту, то она будет помечаться зеленым цветом\n
                            
                            Желаю Удачи!!!
                    
                    """.split("\n")
        self.font = pygame.font.Font(None, 30)
        self.dy = 0

    def __call__(self, screen):
        while True:
            screen.fill(BLACK)
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_exit.is_click():
                        return
                if ev.type == pygame.MOUSEWHEEL:
                    self.dy += -20 * ev.y
            self.draw_text(screen)
            self.button_exit.is_focus(pygame.mouse.get_pos(), dy=self.dy)
            self.button_exit.draw(screen, dy=-self.dy)
            pygame.display.update()

    def draw_text(self, screen):
        for y, line in enumerate(self.text):
            text = self.font.render(line, True, GREY)
            screen.blit(text, (100, y * 30 - self.dy))
