import pygame
import sys
import os

def show_loading_screen(screen):
    try:
        loading_img = pygame.image.load("assets/sprites/loadcscreen.png").convert()
        loading_img = pygame.transform.scale(loading_img, (screen.get_width(), screen.get_height()))
        screen.blit(loading_img, (0, 0))
    except:
        screen.fill((0, 0, 0))

    # Fuente para textos
    font_small = pygame.font.SysFont("Arial", 24)
    font_large = pygame.font.SysFont("Arial", 32, bold=True)

    # Mensaje de entrada
    text = font_small.render("Pulsa una tecla para entrar al laboratorio", True, (255, 255, 255))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() - 60))

    # Mostrar scoreboard
    scoreboard_path = "scoreboard.txt"
    if os.path.exists(scoreboard_path):
        with open(scoreboard_path, "r", encoding="utf-8") as f:
            lines = f.readlines()[-5:]  # Últimos 5
    else:
        lines = []

    scoreboard_title = font_large.render("Últimos resultados", True, (255, 215, 0))
    screen.blit(scoreboard_title, (screen.get_width() // 2 - scoreboard_title.get_width() // 2, 80))

    for i, line in enumerate(reversed(lines)):
        entry = font_small.render(line.strip(), True, (240, 240, 240))
        screen.blit(entry, (screen.get_width() // 2 - entry.get_width() // 2, 130 + i * 30))

    pygame.display.flip()

    # Esperar pulsación
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False