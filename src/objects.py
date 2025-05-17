import pygame

class FallingObject:
    def __init__(self, x, y, kind, image):
        self.kind = kind
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.y = y

    def update(self, speed):
        self.y += speed
        self.rect.y = int(self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def load_images():
    emerald = pygame.image.load("assets/sprites/emerald.png").convert_alpha()
    emerald = pygame.transform.scale(emerald, (40, 40))

    diamond = pygame.image.load("assets/sprites/diamond.png").convert_alpha()
    diamond = pygame.transform.scale(diamond, (40, 40))

    anvil = pygame.image.load("assets/sprites/anvil.png").convert_alpha()
    anvil = pygame.transform.scale(anvil, (50, 50))

    cake = pygame.image.load("assets/sprites/cake.png").convert_alpha()
    cake = pygame.transform.scale(cake, (50, 50))

    return {
        "emerald": emerald,
        "diamond": diamond,
        "anvil": anvil,
        "cake": cake
    }