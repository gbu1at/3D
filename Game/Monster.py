from Game.BFS import *


class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to_player(self, player_pos):
        dist = bfs.get_dist(start_pos=(self.x, self.y), end_pos=player_pos)
        if dist > 15:
            return
        neighbours = bfs.get_neighbours((self.x, self.y))
        for neighbor in neighbours:
            if bfs.get_dist(start_pos=neighbor, end_pos=player_pos) == dist - 1 and is_free_cell(*neighbor):
                self.set_coord(*neighbor)
                return

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if (self.x + dx, self.y + dy, ID_WALL) not in setting.OBJECTS:
            self.x += dx
            self.y += dy
            return True
        return False

    def get_pos(self):
        return self.x, self.y

    def __hash__(self):
        return (self.x, self.y).__hash__()
