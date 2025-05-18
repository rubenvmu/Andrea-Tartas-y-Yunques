import pygame
import random

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


class SideObject:
    def __init__(self, kind, image, screen_width, screen_height):
        self.kind = kind
        self.direction = random.choice(["left", "right"])
        self.speed = random.randint(3, 6)

        # Volteo horizontal si entra por la izquierda
        if self.direction == "right":
            self.image = pygame.transform.flip(image, True, False)
        else:
            self.image = image

        self.rect = self.image.get_rect()

        if self.direction == "left":
            self.rect.left = screen_width
        else:
            self.rect.right = 0

        self.rect.top = random.randint(100, screen_height - 100)

    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def load_images():
    def load_and_scale(path, size):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, size)

    return {
        "emerald": load_and_scale("assets/sprites/emerald.png", (65, 65)),
        "diamond": load_and_scale("assets/sprites/diamond.png", (65, 65)),
        "anvil": load_and_scale("assets/sprites/anvil.png", (65, 65)),
        "cake": load_and_scale("assets/sprites/cake.png", (65, 65)),
        "bus": load_and_scale("assets/sprites/bus.png", (200, 200))  # puedes ajustar a (160, 80) si prefieres
    }