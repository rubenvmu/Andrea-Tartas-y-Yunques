import pygame

def draw_ui(screen, score, lives, font, heart_img, avatar_img):
    # ---------- CONTADOR DE PUNTOS (ARRIBA DERECHA) ----------
    big_font = pygame.font.SysFont("Arial", 36, bold=True)
    gold_color = (255, 215, 0)
    shadow_color = (0, 0, 0)

    # Sombra + texto
    text_surface_shadow = big_font.render(f"Puntos: {score}", True, shadow_color)
    text_surface = big_font.render(f"Puntos: {score}", True, gold_color)

    text_x = screen.get_width() - text_surface.get_width() - 80
    screen.blit(text_surface_shadow, (text_x + 2, 22))
    screen.blit(text_surface, (text_x, 20))

    # ---------- CORAZONES (ARRIBA IZQUIERDA) ----------
    for i in range(lives):
        screen.blit(heart_img, (20 + i * 30, 20))

    # ---------- AVATAR DE ANDREA (ABAJO IZQUIERDA) ----------
    screen.blit(avatar_img, (20, screen.get_height() - 190))