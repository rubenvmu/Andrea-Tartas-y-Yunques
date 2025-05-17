import pygame

class Player:
    def __init__(self, x, y):
        # Cargar sprites
        self.image_right = pygame.image.load("assets/sprites/andreachibi.png").convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right, (100, 100))

        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image_down = pygame.image.load("assets/sprites/andrea_alante.png").convert_alpha()
        self.image_down = pygame.transform.scale(self.image_down, (100, 100))

        self.image_up = pygame.image.load("assets/sprites/andrea_tras.png").convert_alpha()
        self.image_up = pygame.transform.scale(self.image_up, (100, 100))

        # Estado inicial
        self.image = self.image_down
        self.direction = "down"

        self.rect = self.image.get_rect(center=(x, y))

        # Velocidad de movimiento
        self.speed = 5

    def update(self, keys, screen_width, screen_height):
        moved = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = self.image_left
            self.direction = "left"
            moved = True

        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = self.image_right
            self.direction = "right"
            moved = True

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.image = self.image_up
            self.direction = "up"
            moved = True

        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.image = self.image_down
            self.direction = "down"
            moved = True

        # Limitar dentro de la pantalla
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))

    def draw(self, screen):
        screen.blit(self.image, self.rect)