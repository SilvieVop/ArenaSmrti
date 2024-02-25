# chtela bych vložit casovač, aby se welcome zobrazilo cca 2 sekundy po zobrazeni background a musceleteera
# propojeni se zakladni_vstupy a dalsimy soubory


# chtela bych vložit casovač, aby se welcome zobrazilo cca 2 sekundy po zobrazeni background a musceleteera
# propojeni se zakladni_vstupy a dalsimy soubory


import os
import pygame
import sys
import time

import zakladni_vstupy


# Inicializace pygame
pygame.init()

# Velikost okna
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Nastavení okna
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("ArenaSmrti")

# Načtení obrázků
script_dir = os.path.dirname(__file__)
image_folder = os.path.join(script_dir, "image")

background_image = pygame.image.load(os.path.join(image_folder, "background.png"))
musketeer_image = pygame.image.load(os.path.join(image_folder, "muscleteers.png"))
# time.sleep(2) # uplně to nefunguje tak jak jsem chtela..
welcome_image = pygame.image.load(os.path.join(image_folder, "welcome.png")).convert()

# Převedení obrázku na vhodný formát
welcome_image.set_colorkey(WHITE)  # Nastavení bílé barvy jako průhledné

# Změna velikosti obrázků
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
musketeer_image = pygame.transform.scale(musketeer_image, (264, 232))
welcome_image = pygame.transform.scale(welcome_image, (200, 200))

# Font pro textový výstup
font = pygame.font.Font(None, 28)

# Hlavní smyčka hry
running = True


def handle_user_input():
    pass


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            else:
                zakladni_vstupy.handle_user_input()

    # Vykreslení pozadí
    screen.blit(background_image, (0, 0))

    # Vykreslení obrázků
    musketeer_rect = musketeer_image.get_rect()
    musketeer_rect.y = WINDOW_HEIGHT // 3.4 + 100  # Posun obrázku pod střed
    musketeer_rect.x = WINDOW_WIDTH // 4.8 + 100  # Posun obrázku doprava od středu
    musketeer_image.set_colorkey((255, 255, 255))  # Nastavení průhledné barvy bílá
    screen.blit(musketeer_image, musketeer_rect)

    welcome_rect = welcome_image.get_rect()
    welcome_rect.y = WINDOW_HEIGHT // 12 - 100  # Posun obrázku pod střed
    welcome_rect.x = WINDOW_WIDTH // 2 - 100  # Posun obrázku doprava od středu
    screen.blit(welcome_image, welcome_rect)

    # Vykreslení textu na terminál
    terminal_height = 150  # Výška terminálu
    pygame.draw.rect(screen, BLACK, (0, WINDOW_HEIGHT - terminal_height, WINDOW_WIDTH, terminal_height))
    # Vykreslení černého pozadí pro terminál

    # Zde vykreslete text pomocí pygame.draw.text() nebo pygame.font.Font.render() funkce
    text_surface = font.render(f"zde by měl být text ze souboru zakladni_vstupy, zajisteni pres to handle_user_input",
                               True, WHITE)  # Vytvoření textového povrchu s bílou barvou
    screen.blit(text_surface, (20, WINDOW_HEIGHT - terminal_height + 20))  # Vykreslení textu na určenou pozici

    zakladni_vstupy.handle_user_input()   # tohle by mělo zajistit volání souboru zakladni_vstupy a zpracovani uzivatelskych vstupu
    # Aktualizace obrazovky
    pygame.display.update()

pygame.quit()
sys.exit()

