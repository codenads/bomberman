from enum import Enum, auto


class MapObjects(Enum):
    EMPTY = 0
    BLOCK = auto()
    BOX = auto()
    BOMB = auto()
    EXPLOSION = auto()


class Map:
    def __init__(self):
        self.path = [
            [0, 0, 1, 1, 0],
            [0, 2, 1, 0, 0],
            [1, 0, 2, 2, 1],
            [1, 0, 0, 2, 2],
            [1, 1, 1, 1, 1],
        ]
        self.width = 5
        self.height = 5
        self.players = []

    def get(self, x, y):
        if x < self.width and y < self.height:
            return self.path[y][x]  # on player's logic, x and y are inverted

    def set(self, x, y, value):
        if x < self.width and y < self.height:
            self.path[y][x] = value  # on player's logic, x and y are inverted

    def collision(self, x, y):
        return bool(self.get(x, y))

    def print(self):
        for i in range(0, self.width):
            print("[", end=" ")
            for j in range(0, self.height):
                print(self.path[i][j], end=" ")
            print("]")
