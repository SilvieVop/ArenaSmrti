# není hotovo , nevím jestli bude použito

from data_loader import DataLoader

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 155, 255)

        self.data_loader = DataLoader()

        self.zakladni_vstupy_data = self.data_loader.load_zakladni_vstupy()
        self.tri_musketyri_data = self.data_loader.load_tri_musketyri()
        self.arena_musketyri_data = self.dala_loader.load_arena_musketyri()
        self.carodejove_data = self.data_loader.load_carodejove()
        self.arena_carodejove_data = self.data_loader.load_arena_carodejove()

