from server.map import MapObjects


class Bomb:
    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        self.force = 2
        self.explosion = []
        self.create(map)
        self.range(map)

    def create(self, map):
        if map.get(self.x, self.y) != MapObjects.BOMB.value:
            map.set(self.x, self.y, MapObjects.BOMB.value)

    def delete(self, map):
        map.set(self.x, self.y, MapObjects.EMPTY.value)

    def calculate(self, map, x, y):
        if map.get(x, y) != MapObjects.BLOCK.value:
            if (x >= 0 and x <= map.width) and (y >= 0 and y <= map.height):
                self.explosion.append((x, y))

    def range(self, map):
        for length in range(1, self.force + 1):
            self.calculate(map, self.x + length, self.y)

        for length in range(1, self.force + 1):
            self.calculate(map, self.x - length, self.y)

        for length in range(1, self.force + 1):
            self.calculate(map, self.x, self.y + length)

        for length in range(1, self.force + 1):
            self.calculate(map, self.x, self.y - length)

    def explode(self, map):
        for position in self.explosion:
            map.set(position[0], position[1], MapObjects.EXPLOSION.value)
        for position in self.explosion:
            map.set(position[0], position[1], MapObjects.EMPTY.value)
        self.delete(map)
