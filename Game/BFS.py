from ROOT.functions import *
from numba import prange
INF = 1e9


class BFS:
    def __init__(self):
        ...

    def init(self):
        self.size = setting.COLS * setting.ROWS
        self.dist = [[INF for _ in prange(self.size)] for _ in prange(self.size)]
        for i in prange(self.size):
            self.dist[i][i] = 0

        for x in prange(setting.COLS):
            for y in prange(setting.ROWS):
                self.create_min_dist_vertex((x, y))

    def create_min_dist_vertex(self, start):
        S = self.get_vertex(*start)
        l = 0
        r = 1
        q = [start]
        map = set()
        while l < r:
            v = q[l]
            V = self.get_vertex(*v)
            l += 1
            map.add(v)
            neighbours_vertex = self.get_neighbours(v)
            for u in neighbours_vertex:
                if u not in map:
                    map.add(u)
                    q.append(u)
                    U = self.get_vertex(*u)
                    self.dist[S][U] = self.dist[S][V] + 1
                    r += 1

    def get_vertex(self, x, y):
        return y * setting.COLS + x

    def get_coord(self, vertex):
        x = vertex % setting.COLS
        y = vertex // setting.ROWS
        return x, y

    def get_dist(self, start_pos, end_pos):
        S = self.get_vertex(*start_pos)
        E = self.get_vertex(*end_pos)
        return self.dist[S][E]

    def get_neighbours(self, vertex):
        x, y = vertex
        if is_wall_coord(x, y):
            return []
        neighbours = []
        if not is_wall_coord(x + 1, y):
            neighbours.append((x + 1, y))
        if not is_wall_coord(x - 1, y):
            neighbours.append((x - 1, y))
        if not is_wall_coord(x, y + 1):
            neighbours.append((x, y + 1))
        if not is_wall_coord(x, y - 1):
            neighbours.append((x, y - 1))

        return neighbours


bfs = BFS()
