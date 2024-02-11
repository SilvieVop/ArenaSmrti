# v tomto listě jsem chtěla mít především třídu ArenaSmrti
# a co v té aréně budou dělat..
# mělo by to zobrazovat boj po řádcích
# měl by tu být konec boje - jeden z hráčů bude mrtvý
# možná bych mohla mít pouze jednu arenu pro mušketýri i čaroděje..

# sem bych asi měla vložit nějaké argumenty a kwargs pro to aby to bralo ty správné def
from colorama import Fore, Style

from zakladni_vstupy import musketyr1, musketyr2, musketyr3, musketyr4


class ArenaSmrti:
    def __init__(self, *arg, musketyr1, musketyr2, musketyr3, musketyr4):
        self.musketyr1 = musketyr1
        self.musketyr2 = musketyr2
        self.musketyr3 = musketyr3
        self.musketyr4 = musketyr4

# tak ti nevim co s tim... ted uz vůbec zapist nechtěji
    def zapasit(self):
       while (self.musketyr1.zivot > 0 and self.musketyr2.zivot > 0 and self.musketyr3.zivot > 0
              and self.musketyr4.zivot > 0):
            utok_musketyr1 = self.musketyr1.zautoc
            self.musketyr2.bran_se(utok_musketyr1)

            utok_musketyr1 = self.musketyr1.zautoc
            self.musketyr3.bran_se(utok_musketyr1)

            utok_musketyr1 = self.musketyr1.zautoc
            self.musketyr4.bran_se(utok_musketyr1)

            utok_musketyr2 = self.musketyr2.zautoc
            self.musketyr1.bran_se(utok_musketyr2)

            utok_musketyr2 = self.musketyr2.zautoc
            self.musketyr3.bran_se(utok_musketyr2)

            utok_musketyr2 = self.musketyr2.zautoc
            self.musketyr4.bran_se(utok_musketyr2)

            utok_musketyr3 = self.musketyr3.zautoc
            self.musketyr1.bran_se(utok_musketyr3)

            utok_musketyr3 = self.musketyr3.zautoc
            self.musketyr2.bran_se(utok_musketyr3)

            utok_musketyr3 = self.musketyr3.zautoc
            self.musketyr4.bran_se(utok_musketyr3)

            utok_musketyr4 = self.musketyr3.zautoc
            self.musketyr1.bran_se(utok_musketyr4)

            utok_musketyr4 = self.musketyr3.zautoc
            self.musketyr2.bran_se(utok_musketyr4)

            utok_musketyr4 = self.musketyr3.zautoc
            self.musketyr3.bran_se(utok_musketyr4)

            pass

# if self.zivot == 0:
            #     print(Fore.RED + f"{self.jmeno} JE MRTVÝ" + Style.RESET_ALL)
            # # else:
            # #     self.zivot < 0
            # #     print(Fore.RED + f"{self.jmeno} JE TOTÁÁÁÁÁÁLNĚ MRTVÝÝÝÝÝ" + Style.RESET_ALL)

            print(Fore.LIGHTGREEN_EX + f"Konec boje" + Style.RESET_ALL)

            if self.musketyr1.zivot > 0:
                print(Fore.CYAN + f"{self.musketyr1.jmeno} vyhrál!" + Style.RESET_ALL)
            elif self.musketyr2.zivot > 0:
                print(Fore.CYAN + f"{self.musketyr2.jmeno} vyhrál!" + Style.RESET_ALL)
            elif self.musketyr3.zivot > 0:
                print(Fore.CYAN + f"{self.musketyr3.jmeno} vyhrál!" + Style.RESET_ALL)
            elif self.musketyr4.zivot > 0:
                print(Fore.CYAN + f"{self.musketyr4.jmeno} vyhrál!" + Style.RESET_ALL)
            else:
                print(f"NEFUNGUJE TI TO")

