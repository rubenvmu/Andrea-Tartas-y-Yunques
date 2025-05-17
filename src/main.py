import pygame
import random
from src.player import Player
from src.objects import FallingObject, load_images
from src.ui import draw_ui

# Inicialización
pygame.init()
screen_width, screen_height = 1024, 576  # Pantalla horizontal
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cae Química")
clock = pygame.time.Clock()

# Fondo del mapa
background = pygame.image.load("assets/sprites/mapu.png").convert()
background = pygame.transform.scale(background, (screen_width, screen_height))

# Variables de juego
player = Player(screen_width // 2, screen_height - 100)
objects = []
score = 0
lives = 3
fall_speed = 3
spawn_delay = 1000  # milisegundos
last_spawn = pygame.time.get_ticks()
last_speedup = pygame.time.get_ticks()
images = load_images()

running = True
font = pygame.font.SysFont("Arial", 28)

# Bucle principal
while running:
    dt = clock.tick(60)
    screen.blit(background, (0, 0))  # Dibujar fondo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento
    keys = pygame.key.get_pressed()
    player.update(keys, screen_width, screen_height)

    # Acelerar juego cada 2 segundos
    now = pygame.time.get_ticks()
    if now - last_speedup > 2000:
        fall_speed += 0.2
        last_speedup = now

    # Generar objetos
    if now - last_spawn > spawn_delay:
        kind = random.choice(["emerald", "diamond", "anvil"])
        x = random.randint(0, screen_width - 40)
        objects.append(FallingObject(x, -50, kind, images[kind]))
        last_spawn = now

    # Actualizar objetos
    for obj in objects[:]:
        obj.update(fall_speed)
        if obj.rect.colliderect(player.rect):
            if obj.kind == "emerald":
                score += 1
            elif obj.kind == "diamond":
                score += 5
            elif obj.kind == "anvil":
                lives -= 1
            objects.remove(obj)
        elif obj.y > screen_height:
            objects.remove(obj)

    # Dibujar jugador, objetos y UI
    player.draw(screen)
    for obj in objects:
        obj.draw(screen)
    draw_ui(screen, score, lives, font)

    # Comprobar derrota
    if lives <= 0:
        running = False

    pygame.display.flip()

pygame.quit()