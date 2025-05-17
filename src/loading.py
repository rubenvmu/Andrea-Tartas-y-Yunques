import pygame
import sys

def show_loading_screen(screen):
    try:
        loading_img = pygame.image.load("assets/sprites/loadcscreen.png").convert()
        loading_img = pygame.transform.scale(loading_img, (screen.get_width(), screen.get_height()))
        screen.blit(loading_img, (0, 0))
    except:
        screen.fill((0, 0, 0))

    # Texto de carga
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("Pulsa una tecla para entrar al laboratorio", True, (255, 255, 255))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() - 60))

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