# En src/stamina.py
import pygame

class Stamina:
    def __init__(self):
        self.max_stamina = 5
        self.dash_stamina = self.max_stamina
        self.last_use_time = 0
        self.cooldown = 300
        self.blocked_until = 0
        self.full_cooldown = 1500

    def can_dash(self):
        current_time = pygame.time.get_ticks()
        return self.dash_stamina > 0 and current_time > self.blocked_until

    def use(self):
        if self.can_dash():
            self.dash_stamina -= 1
            self.last_use_time = pygame.time.get_ticks()
            if self.dash_stamina == 0:
                self.blocked_until = self.last_use_time + self.full_cooldown

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.dash_stamina < self.max_stamina and current_time > self.blocked_until:
            if current_time - self.last_use_time > self.cooldown:
                self.dash_stamina += 1
                self.last_use_time = current_time

    def draw(self, screen, x, y):
        for i in range(self.max_stamina):
            color = (255, 255, 0) if i < self.dash_stamina else (80, 80, 80)
            pygame.draw.rect(screen, color, (x + i * 35, y, 30, 10), border_radius=3)