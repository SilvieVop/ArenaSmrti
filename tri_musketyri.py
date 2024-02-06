# Co jsem v tomto listu chtěla mít a asi to nějak nevyšlo:
# - popis můšketýrů
# - def jejich vlastnostní jako je utok, obrana a ukazatel života
# - spouští se zde i celý boj mušketýrů .. Nevypisuje se celý.. někde je chyba a Neumírají a nikdo nevyhrává.
# - Chyba - bojují všichni a ne jen ti vybraní ze souboru zakladni_vstupy.py
# ty same problémy u čarodějů


import random

from colorama import Fore, Style

class TriMusketyri:
    pocet_zdravi = 100
    poraneni = 0

    def __init__(self, jmeno, zivot, utok, zraneni, obrana, vybrany_protivnik):
        self.jmeno = jmeno
        self.zivot = zivot
        self.utok = utok
        self.zraneni = zraneni
        self.obrana = obrana
        self.vybrany_protivnik = vybrany_protivnik

    @property # getter
    def zautoc(self):  # Dekorátor ?? kam dát setter a co do něj?? tady chci aby mi to generoval jméno protivnika -> nefunguje
        utok = random.randint(1, self.utok)
        print(f"{self.jmeno} zaútočil na {self.vybrany_protivnik} se silou útoku: {utok}.")
        return utok

    # @vybrany_protivnik.setter
    #     print(vybrany_protivnik)

    def bran_se(self, utok):  # tohle bude platit pro oba pri hre
        obrana = random.randint(1, self.obrana)
        print(f"{self.jmeno} se brání silou: {obrana}.\n")
        return obrana

    def aktualni_zivot(self): # tohle by melo ukazovat, kolik bodů poraneni obdrzel a kolik zbyva zivotů pred smrti
        zivot = self.zivot + self.obrana - self.utok
        poraneni = max(0,self.utok - self.obrana)
        self.zivot -= poraneni

        if zivot > 0:
            print(f"{self.jmeno} utrpěl {poraneni} bodů poškození a jeho zbývající život je {zivot} bodů.")
            # print(f"Zbývající život je {self.zivot} bodů.")

        elif zivot <= 0:
            print(f"{self.jmeno} si připsal {poraneni} bodů ke svému životu")


        else:
            self.zivot = 0
            print(Fore.RED + f"{self.jmeno} JE MRTVÝ" + Style.RESET_ALL)

        return zivot

        # else:
        #     self.zivot < 0
        #     print(Fore.RED + f"{self.jmeno} JE TOTÁÁÁÁÁÁLNĚ MRTVÝÝÝÝÝ" + Style.RESET_ALL)

vybrany_protivnik = "{vybrany_protivnik}" # tak dobrý.. už mi to generuje vybraneho musketyra ale jak mu nadefinuji aby to vzal z listu zakladni_vstupy??

class Sermir(TriMusketyri):
    def __init__(self,jmeno: object,utok: object,zraneni: object,obrana: object,vybrany_protivnik: object) -> object:
        super().__init__(jmeno, 100, utok , zraneni, obrana, vybrany_protivnik)

musketyr1 = Sermir("Athos", 21, 32, 24, [vybrany_protivnik])
musketyr1.bran_se(0)
musketyr1.zautoc
musketyr1.aktualni_zivot()

musketyr2 = Sermir("Porthos", 20, 31, 33, [vybrany_protivnik])
musketyr2.bran_se(0)
musketyr2.zautoc
musketyr2.aktualni_zivot()

musketyr3 = Sermir("Aramis", 20, 23, 26, [vybrany_protivnik])
musketyr3.bran_se(0)
musketyr3.zautoc
musketyr3.aktualni_zivot()

musketyr4 = Sermir("D'Artagnan", 23, 32, 29, [vybrany_protivnik]),
musketyr4.bran_se(0)
musketyr4.zautoc
musketyr4.aktualni_zivot()

vybrany_protivnik = Sermir(jmeno=vybrany_protivnik),
vybrany_protivnik.bran_se(0)
vybrany_protivnik.zautoc
vybrany_protivnik.aktualni_zivot()

