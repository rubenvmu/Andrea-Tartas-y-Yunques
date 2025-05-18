import pygame

def draw_ui(screen, score, lives, font, heart_img, avatar_img, level=1, progress=0.0, player=None):
    # ---------- CONTADOR DE PUNTOS (ARRIBA DERECHA) ----------
    big_font = pygame.font.SysFont("Arial", 36, bold=True)
    gold_color = (255, 215, 0)
    shadow_color = (0, 0, 0)

    text_surface_shadow = big_font.render(f"Puntos: {score}", True, shadow_color)
    text_surface = big_font.render(f"Puntos: {score}", True, gold_color)

    text_x = screen.get_width() - text_surface.get_width() - 80
    screen.blit(text_surface_shadow, (text_x + 2, 22))
    screen.blit(text_surface, (text_x, 20))

    # ---------- CORAZONES (ARRIBA IZQUIERDA) ----------
    for i in range(lives):
        screen.blit(heart_img, (20 + i * 30, 20))

    # ---------- AVATAR DE ANDREA (ABAJO IZQUIERDA) ----------
    avatar_x = 20
    avatar_y = screen.get_height() - 190
    screen.blit(avatar_img, (avatar_x, avatar_y))

    # ---------- BARRA DE EXPERIENCIA (ABAJO IZQUIERDA, JUNTO AL AVATAR) ----------
    try:
        xp_bar = pygame.image.load("assets/sprites/xp_bar.png").convert_alpha()
        xp_bar = pygame.transform.scale(xp_bar, (200, 20))

        bar_x = avatar_x + 200 + 20
        bar_y = avatar_y + 80

        screen.blit(xp_bar, (bar_x, bar_y))

        # Relleno de progreso (dentro de la barra)
        inner_width = int((200 - 4) * progress)
        pygame.draw.rect(screen, (0, 200, 255), (bar_x + 2, bar_y + 2, inner_width, 16))

        # Texto del nivel
        level_font = pygame.font.SysFont("Arial", 22, bold=True)
        level_text = level_font.render(f"Nivel {level}", True, (255, 255, 255))
        screen.blit(level_text, (bar_x + 210, bar_y - 1))

        # ---------- BARRA DE ESTAMINA (justo debajo del XP) ----------
        if player:
            stamina_y = bar_y + 30
            draw_stamina_bar(screen, player, bar_x, stamina_y)

    except Exception as e:
        print(f"Error en draw_ui: {e}")


def draw_stamina_bar(screen, player, x, y):
    try:
        for i in range(5):
            color = (255, 255, 0) if i < player.stamina.dash_stamina else (80, 80, 80)
            rect = pygame.Rect(x + i * 34, y, 30, 8)
            pygame.draw.rect(screen, color, rect, border_radius=3)
    except Exception as e:
        print(f"Error en draw_stamina_bar: {e}")