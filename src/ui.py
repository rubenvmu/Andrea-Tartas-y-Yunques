import pygame

def draw_ui(screen, score, lives, font):
    # Mostrar puntos (arriba derecha)
    score_text = font.render(f"Puntos: {score}", True, (255, 255, 255))
    screen.blit(score_text, (screen.get_width() - score_text.get_width() - 20, 20))

    # Dibujar corazones (arriba izquierda)
    for i in range(lives):
        heart = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(heart, (255, 0, 0), (10, 10), 10)
        screen.blit(heart, (20 + i * 30, 20))