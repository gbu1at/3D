from LoadAnimation.Pendulum import *
from ROOT import setting


class LoadingAnimation:
    def __init__(self, timer, screen):
        self.pendulum = Pendulum()

        self.timer = timer
        self.CLOCK = pygame.time.Clock()
        self.delta_time = 0
        self.FPS = 40
        self.screen = screen

        self.start()

    def start(self):
        while not setting.GAME_INIT:
            self.screen.fill(BLACK)

            self.pendulum.draw(self.screen)
            self.pendulum.move()

            self.delta_time += 1 / self.FPS
            pygame.display.update()
            self.CLOCK.tick(self.FPS)
