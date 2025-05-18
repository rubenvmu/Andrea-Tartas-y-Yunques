import pygame

def ask_username(screen, font):
    input_box = pygame.Rect(312, 250, 400, 50)
    username = ""
    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return username if username.strip() else "Anónimo"
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

        screen.fill((15, 15, 30))
        prompt = font.render("Introduce tu nombre y pulsa ENTER:", True, (255, 255, 255))
        text_surf = font.render(username, True, (255, 255, 255))
        pygame.draw.rect(screen, (100, 100, 255), input_box, border_radius=8)

        screen.blit(prompt, (input_box.x, input_box.y - 50))
        screen.blit(text_surf, (input_box.x + 10, input_box.y + 10))

        pygame.display.flip()