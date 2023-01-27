from random import randint
from Game.Monster import *


class Board:
    def __init__(self, polygon):
        self.polygon = polygon
        self.set_map()

    def set_map(self):
        self.x_s = None
        self.y_s = None
        setting.OBJECTS.clear()
        setting.MONSTER_map.clear()
        setting.ROWS = len(self.polygon)
        setting.COLS = len(self.polygon[0])
        for y, line in enumerate(self.polygon):
            for x, val in enumerate(line):
                if val == "W":
                    setting.OBJECTS.add((x, y, ID_WALL))
                if val == "E":
                    setting.POS_END = (x, y)
                    setting.OBJECTS.add((x, y, ID_END))
                if val == "S":
                    self.x_s, self.y_s = x, y
                if val == "M":
                    setting.OBJECTS.add((x, y, ID_MONSTER))
                    setting.MONSTER_map.append(Monster(x, y))

    def change_pos_end(self):
        if setting.POS_END is not None:
            x, y = setting.POS_END
            setting.OBJECTS.remove((x, y, ID_END))
        x = randint(0, setting.COLS - 1)
        y = randint(0, setting.ROWS - 1)
        while (x, y, ID_WALL) in setting.OBJECTS:
            x = randint(0, setting.COLS - 1)
            y = randint(0, setting.ROWS - 1)
        setting.POS_END = (x, y)
        setting.OBJECTS.add((x, y, ID_END))
        # self.set_map()
