import pygame

def show_loading_screen(screen):
    try:
        loading_img = pygame.image.load("assets/sprites/andreaminimap.png").convert_alpha()
        loading_img = pygame.transform.scale(loading_img, (100, 120))
    except:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        return

    screen.fill((20, 20, 20))
    rect = loading_img.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(loading_img, rect)

    font = pygame.font.SysFont("Arial", 30)
    text = font.render("Cargando laboratorio...", True, (255, 255, 255))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, rect.bottom + 10))

    pygame.display.flip()