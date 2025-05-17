import pygame
import random
from src.player import Player
from src.objects import FallingObject, load_images
from src.ui import draw_ui
from src.loading import show_loading_screen  # ✅ AÑADIDO

# Inicialización
pygame.init()
screen_width, screen_height = 1024, 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Andrea Cakes y Anvils")
clock = pygame.time.Clock()

# Mostrar pantalla de carga
show_loading_screen(screen)  # ✅ AÑADIDO

# Fondo del mapa
background = pygame.image.load("assets/sprites/mapu.png").convert()
background = pygame.transform.scale(background, (screen_width, screen_height))

# Precargar imágenes del UI
heart_img = pygame.image.load("assets/sprites/heart.png").convert_alpha()
heart_img = pygame.transform.scale(heart_img, (24, 24))

avatar_img = pygame.image.load("assets/sprites/andreamedium.png").convert_alpha()
avatar_img = pygame.transform.scale(avatar_img, (200, 200))

# Variables del juego
player = Player(screen_width // 2, screen_height - 100)
objects = []
score = 0
lives = 3
fall_speed = 3
spawn_delay = 1000
last_spawn = pygame.time.get_ticks()
last_speedup = pygame.time.get_ticks()
images = load_images()

running = True
font = pygame.font.SysFont("Arial", 28)

# Bucle principal
while running:
    dt = clock.tick(60)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    player.update(keys, screen_width, screen_height)

    # Aumentar dificultad cada 2 segundos
    now = pygame.time.get_ticks()
    if now - last_speedup > 2000:
        fall_speed += 0.1
        last_speedup = now

    # Generar objetos
    if now - last_spawn > spawn_delay:
        last_spawn = now

        objects_to_spawn = 1
        if score >= 200:
            objects_to_spawn = 4
        elif score >= 50:
            objects_to_spawn = 3

        for _ in range(objects_to_spawn):
            kind = random.choices(
                ["emerald", "diamond", "anvil", "cake"],
                weights=[0.5, 0.1, 0.1, 0.3],
                k=1
            )[0]
            x = random.randint(0, screen_width - 40)
            objects.append(FallingObject(x, -50, kind, images[kind]))

    # Actualizar objetos
    for obj in objects[:]:
        obj.update(fall_speed)
        if obj.rect.colliderect(player.rect):
            if obj.kind == "emerald":
                score += 1
            elif obj.kind == "diamond":
                score += 10
            elif obj.kind == "anvil":
                if not player.is_immortal:
                    lives -= 1
            elif obj.kind == "cake":
                effect = random.choice(["heart", "speed", "immortality"])
                result = player.apply_cake_effect(effect)
                if result == "heal" and lives < 3:
                    lives += 1
            objects.remove(obj)
        elif obj.y > screen_height:
            objects.remove(obj)

    # Dibujar todo
    player.draw(screen)
    for obj in objects:
        obj.draw(screen)
    draw_ui(screen, score, lives, font, heart_img, avatar_img)

    # Condición de derrota
    if lives <= 0:
        running = False

    pygame.display.flip()

pygame.quit()