
from colorama import Fore, Style

from carodejove import carodej1, carodej2, carodej3, carodej4

class ArenaSmrti:
    def __init__(self, carodej1, carodej2, carodej3, carodej4, zapasit, utok, bran_se, zautoc):
        self.carodej1 = carodej1
        self.carodej2 = carodej2
        self.carodej3 = carodej3
        self.carodej4 = carodej4
        self.zapasit = zapasit
        self.utok = utok
        self.bran_se = bran_se
        self.zautoc = zautoc

    def zapasit(self):
       while (self.carodej1.zivot > 0 and self.carodej2.zivot > 0 and self.carodej3.zivot > 0
              and self.carodej4.zivot > 0):

            utok_carodej1 = self.carodej1.zautoc
            self.carodej2.bran_se(utok_carodej1)

            utok_carodej1 = self.carodej1.zautoc
            self.carodej3.bran_se(utok_carodej1)

            utok_carodej1 = self.carodej1.zautoc
            self.carodej4.bran_se(utok_carodej1)

            utok_carodej2 = self.carodej2.zautoc
            self.carodej1.bran_se(utok_carodej2)

            utok_carodej2 = self.carodej2.zautoc
            self.carodej3.bran_se(utok_carodej2)

            utok_carodej2 = self.carodej2.zautoc
            self.carodej4.bran_se(utok_carodej2)

            utok_carodej3 = self.carodej3.zautoc
            self.carodej1.bran_se(utok_carodej3)

            utok_carodej3 = self.carodej3.zautoc
            self.carodej2.bran_se(utok_carodej3)

            utok_carodej3 = self.carodej3.zautoc
            self.carodej4.bran_se(utok_carodej3)

            utok_carodej4 = self.carodej3.zautoc
            self.carodej1.bran_se(utok_carodej4)

            utok_carodej4 = self.carodej3.zautoc
            self.carodej2.bran_se(utok_carodej4)

            utok_carodej4 = self.carodej3.zautoc
            self.carodej3.bran_se(utok_carodej4)

            if self.zivot == 0:
                print(Fore.RED + f"{self.jmeno} JE MRTVÝ" + Style.RESET_ALL)
            else:
                self.zivot < 0
                print(Fore.RED + f"{self.jmeno} JE TOTÁÁÁÁÁÁLNĚ MRTVÝÝÝÝÝ" + Style.RESET_ALL)

            print(Fore.LIGHTGREEN_EX + f"Konec boje" + Style.RESET_ALL)

            if self.carodej1.zivot > 0:
                print(Fore.CYAN + f"{self.carodej1.jmeno} vyhrál!" + Style.RESET_ALL)
            elif self.carodej2.zivot > 0:
                print(Fore.CYAN + f"{self.carodej2.jmeno} vyhrál!" + Style.RESET_ALL)
            elif self.carodej3.zivot > 0:
                print(Fore.CYAN + f"{self.carodej3.jmeno} vyhrál!" + Style.RESET_ALL)
            elif self.carodej4.zivot > 0:
                print(Fore.CYAN + f"{self.carodej4.jmeno} vyhrál!" + Style.RESET_ALL)
            else:
                print(f"NEFUNGUJE TI TO")


# carodej1.zapasit()
# carodej2.zapasit()
# carodej3.zapasit()
# carodej4.zapasit()