# Změnit styl boje s kouzli - zmrazení, ohěň, atd co by šlo použít??


import random

from colorama import Fore, Style

import zakladni_vstupy


def handle_user_input(zakladni_vstupy):

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

        @property # getter
        def zautoc(self):  # Dekorátor ?? kam dát setter a co do něj?? tady chci aby mi to generoval jméno protivnika -> nefunguje
            utok = random.randint(1, self.utok)
            print(f"{self.jmeno} zaútočil na {vybrany_carodej} se silou útoku: {utok}.")
            return utok

        def bran_se(self, utok):  # tohle bude platit pro oba pri hre
            obrana = random.randint(1, self.obrana)
            print(f"{self.jmeno} se brání silou: {obrana}.\n")
            return obrana

        def poraneni(self, poraneni, utok, obrana):
            poraneni = max(0, utok - obrana)
            self.zivot -= poraneni
            return poraneni

        def aktualni_zivot(self):
            zivot = self.zivot + self.obrana - self.utok
            poraneni = self.utok - self.obrana  # Vypočítat poškození bez použití max()
            self.zivot -= max(poraneni,1)  # Snížit život o poškození (alespoň 0)

            if self.zivot > 0:
                print(f"{self.jmeno} utrpěl {max(poraneni,0)} bodů poškození a jeho zbývající život je {self.zivot} bodů.")
            else:
                self.zivot = 0
                print(Fore.RED + f"{self.jmeno} JE MRTVÝ" + Style.RESET_ALL)

            return self.zivot

    vybrany_carodej = [zakladni_vstupy.Carodej] # tohle je stoprocentne blbe

    class Carodej(Carodejove):
        def __init__(self, jmeno, utok, zraneni, obrana, mana, vybrany_carodej):
            super().__init__(jmeno, 10, utok, zraneni, obrana, mana, vybrany_carodej)

    carodej1 = Carodej("Gandalf", 2, 3, 1, 6, vybrany_carodej)
    carodej2 = Carodej("Merlin", 2, 3, 2, 5, vybrany_carodej)
    carodej3 = Carodej("Kaprfíld", 2, 2, 2, 5, vybrany_carodej)
    carodej4 = Carodej("Žito", 3, 2, 2, 5, vybrany_carodej)

    while carodej1.zivot > 0 or carodej2.zivot > 0 or carodej3.zivot > 0 or carodej4.zivot > 0:
        if carodej1.zivot > 0:
            carodej1.bran_se(1)
            carodej1.zautoc
            carodej1.kouzli(mana=1)
            carodej1.aktualni_zivot()
        if carodej2.zivot > 0:
            carodej2.bran_se(1)
            carodej2.zautoc
            carodej2.kouzli(mana=1)
            carodej2.aktualni_zivot()
        if carodej3.zivot > 0:
            carodej3.bran_se(1)
            carodej3.zautoc
            carodej3.kouzli(mana=1)
            carodej3.aktualni_zivot()
        if carodej4.zivot > 0:
            carodej4.bran_se(1)
            carodej4.kouzli(mana=1)
            carodej4.zautoc
            carodej4.aktualni_zivot()
