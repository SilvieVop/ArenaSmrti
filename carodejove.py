import random

from colorama import Fore, Style

import bonus_zbrane # zde jsem si myslela, že použijí zbran pouze v případě bonusu.. dá se ještě předělat

import zakladni_vstupy


class Carodejove():
    def __init__(self, jmeno, zivot, utok, zraneni, obrana, mana, vybrany_carodej):
        self.jmeno = jmeno
        self.zivot = zivot
        self.utok = utok
        self.zraneni = zraneni
        self.obrana = obrana
        self.mana = mana
        self.vybrany_carodej = vybrany_carodej


    def predstav_se(self) -> object:
        if "Gandalf" == self.jmeno:
            print(Fore.BLUE + f"Jmenuji se Gandalf. Gandalf Bílý ty prevíte Nazghúle\n" + Style.RESET_ALL)
        elif "Merlin" == self.jmeno:
            print(Fore.GREEN + f"Kdo se opovažuje budit mocného kouzelníka Merlina. Strestám tě jak bídného psa... \n" + Style.RESET_ALL)
        elif "Kaprfíld" == self.jmeno:
            print(Fore.YELLOW + f"Čau já jsem Dejf... Dejf Kaprfíld\n" + Style.RESET_ALL)
        elif "Kouzelník Žito" == self.jmeno:
            print(Fore.RED + f"Tvářím se přátelsky ale zmlátím tě tak, jako že se Kouzelník Žito jmenuji.\n" + Style.RESET_ALL)
        else:
            print(f"Už s tebou nechce nikdo bojovat... HA HA HA\n")

    def kouzli(self, mana):
        kouzlo = random.randint(1, self.mana)
        print(f" {self.jmeno} seslal kouzlo na {self.vybrany_carodej} se silou: {mana}")
        assert isinstance(kouzlo, object)
        return kouzlo

    @property
    def zautoc(self):
        if bonus_zbrane: True
        utok = random.randint(1,self.utok)
        print(f"{self.jmeno} zaútočil na {self.vybrany_carodej} se silou útoku: {utok}.")
        return utok

    def bran_se(self):
        obrana = random.randint(1, self.obrana)
        print(f"{self.jmeno} se brání silou: {obrana}.\n")
        return obrana

    def poraneni(self, poraneni, utok, obrana):
        poraneni = max(0, utok - obrana)
        self.zivot -= poraneni
        return poraneni

    def aktualni_zivot(self, poraneni=None): # tohle by melo ukazovat, kolik bodů poraneni obdrzel a kolik zbyva zivotů pred smrti
        zivot = self.zivot + self.obrana - self.utok
        if zivot > 0:
            print(f"{self.jmeno} utrpěl {poraneni} bodů poškození a jeho zbývající život je {zivot} bodů.")
            # print(f"Zbývající život je {self.zivot} bodů.")

        elif zivot <= 0:
            print(f"{self.jmeno} si připsal {poraneni} bodů ke svému životu")
            return zivot

        else:
            self.zivot = 0
            print(Fore.RED + f"{self.jmeno} JE MRTVÝ" + Style.RESET_ALL)

vybrany_carodej = "{vybrany_carodej}" # tak dobrý.. už mi to generuje vybraneho musketyra ale jak mu nadefinuji aby to vzal z listu zakladni_vstupy??

class Carodej(Carodejove):
    def __init__(self, jmeno, utok, zraneni, obrana, kouzla):
        super(). __init__(jmeno, 100, utok, zraneni, obrana, kouzla)

carodej1 = Carodejove("Gandalf", 21, 32, 24, 10, 10, [vybrany_carodej])
carodej1.kouzli(10)
carodej1.zautoc()
carodej1.bran_se()
carodej1.aktualni_zivot()

carodej2 = Carodejove("Merlin", 20, 31, 33, 10, 10, [vybrany_carodej])
carodej2.kouzli(10)
carodej2.zautoc()
carodej2.bran_se()
carodej2.aktualni_zivot()

carodej3 = Carodejove("Kaprfíld", 20, 23, 26, 10, 10,[vybrany_carodej])
carodej3.kouzli(10)
carodej3.zautoc()
carodej3.bran_se()
carodej3.aktualni_zivot()

carodej4 = Carodejove("Žito", 19, 32, 29, 10, 10, [vybrany_carodej])
carodej4.kouzli(10)
carodej4.zautoc()
carodej4.bran_se()
carodej4.aktualni_zivot()

# TODO zapojit vybrnyho protivnika čarodeje!! zatim nefunguje
vybrany_carodej = Carodejove(jmeno=[vybrany_carodej])
vybrany_carodej.kouzli(10)
vybrany_carodej.zautoc()
vybrany_carodej.bran_se()
vybrany_carodej.aktualni_zivot()
