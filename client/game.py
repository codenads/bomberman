import sys, pygame


class ClientGame:
    def __init__(self):
        self.width = 293
        self.height = 248
        self.size = (self.width, self.height)
        self.speed = [2, 2]
        self.screen = None
        self.background = None
        self.running = False
        self.pygame = pygame

    def setup(self):
        self.background = pygame.image.load("assets/background.png")

    def convert_loaded_images(self):
        self.background.convert()

    def start(self):
        self.pygame.init()
        self.screen = pygame.display.set_mode(self.size)

        self.convert_loaded_images()
        self.screen.blit(self.background, [0, 0])
        self.pygame.display.flip()

        self.running = True

    def end(self):
        pygame.quit()

    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            sys.exit()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.event(event)
