# Není hotovo, nevím jestli bude vůbec použito
# obrázky ?? bmp nebo mohu i Jpg ??

import pygame
import sys

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 155, 255)

class DataLoader:
    def __init__(self):
        pass

    def load_zakladni_vstupy(self, zakladni_vstupy):
        self.zakladni_vstupy = zakladni_vstupy
        # Mělo by to načíst vstupy ze zakladny_vstupy

    def load_tri_musketyri(self, tri_musketyri):
        self.tri_musketyri = tri_musketyri
        # Načte data ze souboru tri_musketyri

    def load_arena_musketyri(self, arena_musketyri):
        self.arena_musketyri = arena_musketyri

    def load_carodejove(self, carodejove):
        self.carodejove = carodejove

    def load_arena_carodejove(self, arena_carodejove):
        self.arena_carodejove = carodejove

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.data_loader = DataLoader()
        self.data_loader.load_zakladni_vstupy("zakladni_vstupy.py")
        self.data_loader.load_tri_musketyri("tri_musketyri.py")
        self.data_loader.load_arena_musketyri("arena_musketyr.py")
        self.data_loader.load_carodejove("carodejove.py")
        self.data_loader.load_arena_carodejove("arena_carodejove.py")
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run_game()
