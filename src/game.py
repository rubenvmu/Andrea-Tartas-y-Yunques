import pygame
from src.map import LabMap
from src.player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.map = LabMap(self.screen)
        self.player = Player(100, 100)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw(self.screen, self.player)
        self.player.draw(self.screen)
        pygame.display.flip()