import pygame
import time
from src.stamina import Stamina

class Player:
    def __init__(self, x, y):
        self.image_right = pygame.image.load("assets/sprites/andreachibi.png").convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right, (100, 100))
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image_down = pygame.image.load("assets/sprites/andrea_alante.png").convert_alpha()
        self.image_down = pygame.transform.scale(self.image_down, (100, 100))
        self.image_up = pygame.image.load("assets/sprites/andrea_tras.png").convert_alpha()
        self.image_up = pygame.transform.scale(self.image_up, (100, 100))

        self.image = self.image_down
        self.direction = "down"
        self.rect = self.image.get_rect(center=(x, y))

        self.base_speed = 5
        self.speed = self.base_speed

        self.is_immortal = False
        self.immortal_timer = 0
        self.speed_boost_timer = 0
        self.magnet_timer = 0

        self.halo_img = pygame.image.load("assets/sprites/halo.png").convert_alpha()
        self.halo_img = pygame.transform.scale(self.halo_img, (60, 30))

        self.alasangel_img = pygame.image.load("assets/sprites/alasangel.png").convert_alpha()
        self.alasangel_img = pygame.transform.scale(self.alasangel_img, (120, 60))

        self.magnet_img = pygame.image.load("assets/sprites/iman.png").convert_alpha()
        self.magnet_img = pygame.transform.scale(self.magnet_img, (40, 40))

        self.last_space_time = 0
        self.space_pressed_once = False

        self.stamina = Stamina()

    def update(self, keys, screen_width, screen_height):
        current_time = pygame.time.get_ticks()
        self.stamina.update()

        if keys[pygame.K_SPACE]:
            if not self.space_pressed_once:
                self.space_pressed_once = True
                self.last_space_time = current_time
            elif current_time - self.last_space_time < 200:
                if self.stamina.can_dash():
                    self.stamina.use()
                    self.megajump()
                self.space_pressed_once = False
        else:
            if self.space_pressed_once and current_time - self.last_space_time > 200:
                self.space_pressed_once = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = self.image_left
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = self.image_right
            self.direction = "right"

        if self.speed > self.base_speed:
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
                self.image = self.image_up
                self.direction = "up"
            elif keys[pygame.K_DOWN]:
                self.rect.y += self.speed
                self.image = self.image_down
                self.direction = "down"
        elif keys[pygame.K_DOWN] or keys[pygame.K_UP]:
            pass

        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))

        if self.speed_boost_timer > 0 and current_time > self.speed_boost_timer:
            self.speed = self.base_speed
            self.speed_boost_timer = 0

        if self.immortal_timer > 0 and current_time > self.immortal_timer:
            self.is_immortal = False
            self.immortal_timer = 0

        if self.magnet_timer > 0 and current_time > self.magnet_timer:
            self.magnet_timer = 0

        if self.speed == self.base_speed and self.rect.bottom < screen_height:
            self.rect.y += self.base_speed

    def megajump(self):
        jump_distance = 30
        if self.direction == "left":
            self.rect.x -= jump_distance
        elif self.direction == "right":
            self.rect.x += jump_distance
        elif self.direction == "up":
            self.rect.y -= jump_distance
        elif self.direction == "down":
            self.rect.y += jump_distance

    def apply_cake_effect(self, effect):
        current_time = pygame.time.get_ticks()
        if effect == "speed":
            self.speed = self.base_speed + 5
            self.speed_boost_timer = current_time + 10000
        elif effect == "immortality":
            self.is_immortal = True
            self.immortal_timer = current_time + 5000
        elif effect == "magnet":
            self.magnet_timer = current_time + 2500
            return "magnet"

    def has_magnet(self):
        return self.magnet_timer > pygame.time.get_ticks()

    def draw(self, screen):
        if self.speed > self.base_speed:
            wings_x = self.rect.centerx - self.alasangel_img.get_width() // 2
            wings_y = self.rect.top + 20
            screen.blit(self.alasangel_img, (wings_x, wings_y))

        screen.blit(self.image, self.rect)

        if self.is_immortal:
            halo_x = self.rect.centerx - self.halo_img.get_width() // 2
            halo_y = self.rect.top - 10
            screen.blit(self.halo_img, (halo_x, halo_y))

        if self.has_magnet():
            magnet_x = self.rect.centerx - self.magnet_img.get_width() // 2
            magnet_y = self.rect.top - 30
            screen.blit(self.magnet_img, (magnet_x, magnet_y))
