import pygame

def pause_game(screen, screen_width, screen_height):
    pause_font = pygame.font.SysFont("Arial", 48, bold=True)
    small_font = pygame.font.SysFont("Arial", 24)
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False

        screen.fill((15, 15, 30))
        title = pause_font.render("⏸ PAUSA", True, (255, 255, 255))
        info = small_font.render("Pulsa ESC para continuar", True, (180, 180, 180))

        screen.blit(title, (screen_width // 2 - title.get_width() // 2, screen_height // 2 - 60))
        screen.blit(info, (screen_width // 2 - info.get_width() // 2, screen_height // 2 + 10))

        pygame.display.flip()