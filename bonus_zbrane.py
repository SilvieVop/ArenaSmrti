# TODO List
# v tomto souboru bych chtěla definovat bonusové zbraně
# chtěla jsem vložit draka ale spíš bude lepší udělat bonusové kolo s drakem
# nebo bych to mohla pojmout jako bonusové kolo s bonusovou zbraní... draka přece jen tak párátkem nezabiješ :D
# bonusové kolo by mohlo být po třech vítěztví v řadě..
# po totální výhře by se mohl zobrazit obrázek něco jako ArenaWinner
from random import random


class bonus_zbran:
    def __init__(self, cool_mec, fire_kladivo, heavy_stit, other_drak):
        self.cool_mec = cool_mec
        self.fire_kladivo = fire_kladivo
        self.heavy_stit = heavy_stit
        self.other_drak = other_drak

    def cool_mec(self):
        cool_mec = random.randint(self.cool_mec, 1, 3)  # tady aby to generoval zranění od 1 do 3

    def fire_kladivo(self):
        fire_kladivo = random.randint(self.fire_kladivo(), 1, 3)

    def heavy_stit(self):
        heavy_stit = random.randint(self.heavy_stit(), 1, 4)  # zde obrana 1 až 4 boy ??


class Drak:
    pocet_zdravi = None

    def __init__(self, ohen, mavnuti_kridly):
        self.ohen = ohen
        self.mavnuti_kridly = mavnuti_kridly  # tím bude odrázet utoky.. něco jako obrana

    def blokace_utoku(self):
        pass

    def plivanec(self):
        pass
