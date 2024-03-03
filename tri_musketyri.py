# Co jsem v tomto listu chtěla mít a asi to nějak nevyšlo:
# - popis můšketýrů
# - def jejich vlastnostní jako je utok, obrana a ukazatel života
# TODO list
# - všichni umírají
# - Chyba - bojují všichni a ne jen ti vybraní ze souboru zakladni_vstupy.
# Stejné problém jsou v listu carodejove.py


import random

from colorama import Fore, Style

import zakladni_vstupy


def handle_user_input(zakladni_vstupy):

    class TriMusketyri:

        def __init__(self, jmeno, zivot, utok, zraneni, obrana, vybrany_protivnik):
            self.jmeno = jmeno
            self.zivot = zivot
            self.utok = utok
            self.zraneni = zraneni
            self.obrana = obrana
            self.vybrany_protivnik = vybrany_protivnik

        # @property # getter
        def zautoc(self):  # Dekorátor ?? kam dát setter a co do něj?? tady chci aby mi to generoval jméno protivnika -> nefunguje
            utok = random.randint(1, self.utok)
            print(f"{self.jmeno} zaútočil na {vybrany_protivnik} se silou útoku: {utok}.")
            return utok

        def bran_se(self, utok):  # tohle bude platit pro oba pri hre
            obrana = random.randint(1, self.obrana)
            print(f"{self.jmeno} se brání silou: {obrana}.\n")
            return obrana

        def aktualni_zivot(self):
            zivot = self.zivot + self.obrana - self.utok
            poraneni = self.utok - self.obrana  # Vypočítat poškození bez použití max()
            self.zivot -= max(poraneni, 1)  # Snížit život o poškození (alespoň 0)

            if self.zivot > 0:
                print(f"{self.jmeno} utrpěl {max(poraneni,0)} bodů poškození a jeho zbývající život je {self.zivot} bodů.")
            else:
                self.zivot = 0
                print(Fore.RED + f"{self.jmeno} JE MRTVÝ" + Style.RESET_ALL)

            return self.zivot

    vybrany_protivnik = [zakladni_vstupy.Musketyr] # tohle je blbe.. uplně to neukazuje cestu odkud to má brát..
    class Sermir(TriMusketyri):
        def __init__(self, jmeno, utok, zraneni, obrana, vybrany_protivnik):
            super().__init__(jmeno, 10, utok, zraneni, obrana, vybrany_protivnik)

    musketyr1 = Sermir("Athos", 2, 3, 2, vybrany_protivnik)
    musketyr2 = Sermir("Porthos", 2, 1, 3, vybrany_protivnik)
    musketyr3 = Sermir("Aramis", 2, 3, 2, vybrany_protivnik)
    musketyr4 = Sermir("D'Artagnan", 3, 2, 2, vybrany_protivnik)

    while musketyr1.zivot > 0 or musketyr2.zivot > 0 or musketyr3.zivot > 0 or musketyr4.zivot > 0:
        if musketyr1.zivot > 0:
            musketyr1.bran_se(1)
            musketyr1.zautoc()
            musketyr1.aktualni_zivot()
        if musketyr2.zivot > 0:
            musketyr2.bran_se(1)
            musketyr2.zautoc()
            musketyr2.aktualni_zivot()
        if musketyr3.zivot > 0:
            musketyr3.bran_se(1)
            musketyr3.zautoc()
            musketyr3.aktualni_zivot()
        if musketyr4.zivot > 0:
            musketyr4.bran_se(1)
            musketyr4.zautoc()
            musketyr4.aktualni_zivot()
        break

