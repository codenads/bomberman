from bomb import Bomb
from time import sleep


class Player:
    def __init__(self, x, y, username):
        self.username = username
        self.x = x
        self.y = y
        self.life = True
        self.moves = {
            "up": self.up,
            "down": self.down,
            "left": self.left,
            "right": self.right,
            "bomb": self.bomb,
        }

    def up(self, map):
        if self.y > 0:
            if not map.collision(self.x, self.y - 1):
                self.y -= 1

    def down(self, map):
        if self.y < map.height - 1:
            if not map.collision(self.x, self.y + 1):
                self.y += 1

    def left(self, map):
        if self.x > 0:
            if not map.collision(self.x - 1, self.y):
                self.x -= 1

    def right(self, map):
        if self.x < map.width - 1:
            if not map.collision(self.x + 1, self.y):
                self.x += 1

    def bomb(self, map):
        bomb = Bomb(self.x, self.y, map)
        bomb.explode(map)
        del bomb

    def move(self, command, map):
        if command in self.moves.keys():
            self.moves[command](map)
            print("Player {} is at: ({}, {})".format(self.username, self.x, self.y))
            map.print()
        else:
            print("Invalid command.")
