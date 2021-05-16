import pygame


class ClientGame:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.size = (500, 500)
        self.speed = [2, 2]
        self.screen = None
        self.running = False

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.running = True

    def end(self):
        pygame.quit()

    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.event(event)
