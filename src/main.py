import pygame
import random
from src.player import Player
from src.objects import FallingObject, SideObject, load_images
from src.ui import draw_ui
from src.loading import show_loading_screen
from src.level_system import LevelSystem
from src.username_input import ask_username
from src.scoreboard import save_score
from src.pause_menu import pause_game

pygame.init()
screen_width, screen_height = 1024, 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Andrea Cakes y Anvils")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

username = ask_username(screen, font)
show_loading_screen(screen)

background = pygame.image.load("assets/sprites/mapu.png").convert()
background = pygame.transform.scale(background, (screen_width, screen_height))

heart_img = pygame.image.load("assets/sprites/heart.png").convert_alpha()
heart_img = pygame.transform.scale(heart_img, (24, 24))

avatar_img = pygame.image.load("assets/sprites/andreamedium.png").convert_alpha()
avatar_img = pygame.transform.scale(avatar_img, (200, 200))

images = load_images()

def reset_game():
    return {
        "player": Player(screen_width // 2, screen_height - 100),
        "objects": [],
        "side_objects": [],
        "score": 0,
        "lives": 5,
        "fall_speed": 3,
        "level_system": LevelSystem(points_per_level=50),
        "last_spawn": pygame.time.get_ticks(),
        "last_speedup": pygame.time.get_ticks(),
        "last_bus_spawn": pygame.time.get_ticks(),
    }

state = reset_game()
running = True

while running:
    dt = clock.tick(60)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pause_game(screen, screen_width, screen_height)

    keys = pygame.key.get_pressed()
    state["player"].update(keys, screen_width, screen_height)

    now = pygame.time.get_ticks()
    if now - state["last_speedup"] > 2000:
        state["fall_speed"] += 0.1
        state["last_speedup"] = now

    if now - state["last_spawn"] > 1000:
        state["last_spawn"] = now
        n = 1
        if state["score"] >= 200:
            n = 4
        elif state["score"] >= 50:
            n = 3
        for _ in range(n):
            kind = random.choices(
                ["emerald", "diamond", "anvil", "cake"],
                weights=[0.5, 0.15, 0.2, 0.15],
                k=1
            )[0]
            x = random.randint(0, screen_width - 40)
            state["objects"].append(FallingObject(x, -50, kind, images[kind]))

    if now - state["last_bus_spawn"] > 8000:
        state["side_objects"].append(SideObject("bus", images["bus"], screen_width, screen_height))
        state["last_bus_spawn"] = now

    for obj in state["objects"][:]:
        obj.update(state["fall_speed"])
        if obj.rect.colliderect(state["player"].rect):
            if obj.kind == "emerald":
                state["score"] += 1
            elif obj.kind == "diamond":
                state["score"] += 10
            elif obj.kind == "anvil" and not state["player"].is_immortal:
                state["lives"] -= 1
            elif obj.kind == "cake":
                effect = random.choice(["heart", "speed", "immortality"])
                result = state["player"].apply_cake_effect(effect)
                if result == "heal" and state["lives"] < 5:
                    state["lives"] += 1
            state["objects"].remove(obj)
        elif obj.y > screen_height:
            state["objects"].remove(obj)

    for side in state["side_objects"][:]:
        side.update()
        side.draw(screen)
        if side.rect.colliderect(state["player"].rect):
            if not state["player"].is_immortal:
                state["lives"] -= 1
                state["side_objects"].remove(side)
                continue
        if side.rect.right < 0 or side.rect.left > screen_width:
            state["side_objects"].remove(side)

    state["level_system"].update(state["score"])
    level = state["level_system"].get_level()
    progress = state["level_system"].get_progress(state["score"])

    state["player"].draw(screen)
    for obj in state["objects"]:
        obj.draw(screen)
    draw_ui(screen, state["score"], state["lives"], font, heart_img, avatar_img, level, progress)

    if state["lives"] <= 0:
        save_score(username, state["score"])
        show_loading_screen(screen)
        state = reset_game()

    pygame.display.flip()


pygame.quit()