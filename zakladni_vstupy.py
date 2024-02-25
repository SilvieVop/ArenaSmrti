# Zde jsou základní otázky pro výběr bojovníka, vybrání náhodného protivníka a představení bojovníků.
import pygame
import random
from colorama import Fore, Style

def handle_user_input():
    global one_letter
    one_letter = True

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Zakladní otázky + zakladní výber mezi skupinami
                print("Vítejte")
                print("Zvolte si skupinu svých bojovníků. Dáte přednost MUŠKETÝRŮM či ČARODĚJŮM.")
                print("Jednodušše napiš")
                print(Fore.RED + "M" + Style.RESET_ALL)
                print("pro Mušketýri či")
                print(Fore.GREEN + "C" + Style.RESET_ALL)
                print("pro Čaroděje.")
                one_letter = input("Použij VELKÁ písmena: ").upper()
            else:
                print(f"Výběr nerozpoznán")

    def predstaveni_musketyra(musketyr):  #PRESUNUTO NA KONEC - je to tak dobře??? uplně nevim
        musketyri_popis = {
            "Aramis": Fore.GREEN + f"Jmenuji se Aramis a rozpíchám tě jako jehelníček.. "
                                   f"MHUA MHUA MHUA\n" + Style.RESET_ALL,
            "Athos": Fore.BLUE + f"Jmenuji se Athos a dnes budu tvým poslem smrti, "
                                 f"ty zákeřný pavouku!!!\n" + Style.RESET_ALL,
            "D'Artagnan": Fore.RED + f"Jmenuji se D'Artagnan a doufám, "
                                     f"že máš závěť napsanout... CHA CHA\n" + Style.RESET_ALL,
            "Porthos": Fore.YELLOW + f"Jako že se Porthos jmenuji, tak Vás utopím v Portském víně jako mouchu..."
                                     f" GLO GLO GLO\n" + Style.RESET_ALL
        }
        popis = musketyri_popis.get(musketyr)
        print(f"{musketyr}: {popis}")

    def predstaveni_carodej(carodej):
        carodej_popis = {
            "Gandalf": Fore.BLUE + f"Dobrý den, Gandalf jméno mé.. Podívejte na můj ohňostroj, který tě zničí "
                                   f"... CHA CHA CHA\n" + Style.RESET_ALL,
            "Merlin": Fore.GREEN + f"Jsem mocný čarodej Merlin - Král stromů, rostlin, zvířectva a teď jsem i tvůj PÁN.. "
                                   f"MHUA MHUA MHUA!!!\n" + Style.RESET_ALL,
            "Kaprfíld": Fore.RED + f"Čauves jsem Dejv.. Dejv Kaprfíld. Znáš nějaký kouzelnický trik.. tak koukej, koukej.."
                                   f" AHAAA to jsem tě napálil viď\n" + Style.RESET_ALL,
            "Žito": Fore.YELLOW + f"Jako že se kouzelník Žito jmenuji, tak z tebe vymlátím duši..."
                                  f" HA HA HA\n" + Style.RESET_ALL
        }
        popis = carodej_popis.get(carodej)
        print(f"{carodej}: {popis}")

    # SKUPINA MUSKETYR/SERMIR/mělo by se přenášet i do listu tri_musketyri
    if one_letter == "M":
        print("Výborně... vybral jsi si skupinu:")
        print(Fore.RED + "MUŠKETÝŘI" + Style.RESET_ALL)
        # Vyberte si mušketýra

        musketyr_vyber_a = input("Vyberte ze čtyř mušketýrů, použij první VELKÉ písmeno jména "
                                 "(Aramis, Athos, D'Artagnan, Porthos):"
                                 "HINT: V případě Aramise a Athose použijte druhé písmeno.").upper()

        def vyber_musketyra_popis(musketyr_vyber_a):
            musketyri_popis = {
                "R": Fore.GREEN + "Aramis Jehelníček je známý svým šarmem a šikovností s mečem." + Style.RESET_ALL,
                "T": Fore.BLUE + "Athos je nejstarší a nejvíce záhadný ze skupiny mušketýrů." + Style.RESET_ALL,
                "D": Fore.RED + "D'Artagnan je mladý a odvážný muž, "
                                "který se právě připojil k mušketýrům." + Style.RESET_ALL,
                "P": Fore.YELLOW + "Porthos je obří muž s velkým srdcem a oblibou v dobrém jídle a pití." + Style.RESET_ALL
            }
            popis = musketyri_popis.get(musketyr_vyber_a, "Popis není k dispozici.")
            return popis

        if musketyr_vyber_a == "R":
            musketyr3 = "Aramis"
            print("Vybral jste si:")
            print(Fore.GREEN + "Aramise Jehelníčka." + Style.RESET_ALL)
            print(f"{vyber_musketyra_popis(musketyr_vyber_a)}")
            co_zbylo = ["Athos", "D'Artagnan", "Porthos"]
            vybrany_musketyr = random.choice(co_zbylo)
            print(f"Byl Vám vybrán protivník {vybrany_musketyr}")
            predstaveni_musketyra(vybrany_musketyr)

        elif musketyr_vyber_a == "T":
            musketyr1 = "Athos"
            print("Vybral jste si:")
            print(Fore.BLUE + "Athose Zoufalce." + Style.RESET_ALL)
            print(f"{vyber_musketyra_popis(musketyr_vyber_a)}")
            co_zbylo = ["Aramis", "D'Artagnan", "Porthos"]
            vybrany_musketyr = random.choice(co_zbylo)
            print(f"Byl Vám vybrán protivník {vybrany_musketyr}")
            predstaveni_musketyra(vybrany_musketyr)

        elif musketyr_vyber_a == "D":
            musketyr4 = "D'Artagnan"
            print("Vybral jste si:")
            print(Fore.RED + "D'Artagnana Kravou lázeň." + Style.RESET_ALL)
            print(f"{vyber_musketyra_popis(musketyr_vyber_a)}")
            co_zbylo = ["Aramis", "Athos", "Porthos"]
            vybrany_musketyr = random.choice(co_zbylo)
            print(f"Byl Vám vybrán protivník {vybrany_musketyr}")
            predstaveni_musketyra(vybrany_musketyr)

        elif musketyr_vyber_a == "P":
            musketyr2 = "Porthos"
            print("Vybral jste si:")
            print(Fore.YELLOW + "Porthose Ožralu." + Style.RESET_ALL)
            print(f"{vyber_musketyra_popis(musketyr_vyber_a)}")
            co_zbylo = ["Aramis", "D'Artagnan", "Athos"]
            vybrany_musketyr = random.choice(co_zbylo)
            print(f"Byl Vám vybrán protivník {vybrany_musketyr}")
            predstaveni_musketyra(vybrany_musketyr)

        else:
            print("Nerozpoznáno. Zvolte jednoho ze čtyř mušketýrů R, T, D, P.")

    # SKUPINA ČARODĚJOVÉ - opět přenos do list carodejove.py
    elif one_letter == "C":
        print("Výborně vybral jsi si skupinu:")
        print(Fore.GREEN + 'ČARODĚJOVÉ' + Style.RESET_ALL)

        # Vyberte si čaroděje
        vybrany_carodej_a = input(f"Vyberte si jednoho ze čtyř čarodejů: Gandalf, Merlin, Kaprfíld, Žito:"
                                  f"HINT: U Žita dejte Z - tj. bez háčku. \n").upper()

        def vyber_carodeje_popis(vybrany_carodej_a):
            carodej_popis = {
                "G": Fore.BLUE + "Gandalf Bílý je známý svými skvělími ohňostroji. "
                                 "Vždy je to nezapomenutelná šou." + Style.RESET_ALL,
                "M": Fore.GREEN + "Merlin je lesní muž, který vyhledává samotu a je velice ale "
                                  "velice nedůvěřivý k ostatním." + Style.RESET_ALL,
                "K": Fore.RED + "Kaprfíld je to takový šoumen. Rád baví lidi a utahuje si z nich." + Style.RESET_ALL,
                "Z": Fore.YELLOW + "S kouzelníkem Žitem si jen tak nikdo nezahrává" + Style.RESET_ALL
            }
            popis = carodej_popis.get(vybrany_carodej_a, "Popis není k dispozici.")
            return popis

        if vybrany_carodej_a == "G":
            carodej1 = "Gandalf"
            print(f"Vybral jsi si mocného čaroděje:")
            print(Fore.BLUE + "Gandalfa Bílého" + Style.RESET_ALL)
            print(f"{vyber_carodeje_popis(vybrany_carodej_a)}")
            carodej_zbyl = ["Merlin", "Kaprfíld", "Žito"]
            vybrany_carodej = random.choice(carodej_zbyl)
            print(f"Byl Vám vybrán protivník {vybrany_carodej}")
            predstaveni_carodej(vybrany_carodej)

        elif vybrany_carodej_a == "M":
            carodej2 = "Merlin"
            print(f"Vybral jsi si:")
            print(Fore.GREEN + "Merlina vládce lesů" + Style.RESET_ALL)
            print(f"{vyber_carodeje_popis(vybrany_carodej_a)}")
            carodej_zbyl = ["Gandalf", "Kaprfíld", "Žito"]
            vybrany_carodej = random.choice(carodej_zbyl)
            print(f"Byl Vám vybrán protivník {vybrany_carodej}")
            predstaveni_carodej(vybrany_carodej)

        elif vybrany_carodej_a == "K":
            carodej3 = "Kaprfíld"
            print(f"Vybral jsi si trhlého:")
            print(Fore.RED + "Dejva Kaprfílda" + Style.RESET_ALL)
            print(f"{vyber_carodeje_popis(vybrany_carodej_a)}")
            carodej_zbyl = ["Merlin", "Gandalf", "Žito"]
            vybrany_carodej = random.choice(carodej_zbyl)
            print(f"Byl Vám vybrán protivník {vybrany_carodej}")
            predstaveni_carodej(vybrany_carodej)

        elif vybrany_carodej_a == "Z":
            carodej4 = "Žito"
            print(f"Vybral jsi si šíleného:")
            print(Fore.YELLOW + "kouzelníka Žita" + Style.RESET_ALL)
            print(f"{vyber_carodeje_popis(vybrany_carodej_a)}")
            carodej_zbyl = ["Merlin", "Kaprfíld", "Gandalf"]
            vybrany_carodej = random.choice(carodej_zbyl)
            print(f"Byl Vám vybrán protivník {vybrany_carodej}")
            predstaveni_carodej(vybrany_carodej)

        else:
            print(f"Výběr nerozpoznán. Zvolte platné možnosti G, M, K, Z. ")

    else:
        print("Nerozpoznáno. Zvolte platnou možnost 'M' nebo 'C'.")



    # zjištění typu - stále mi to hází nějakou že "int" object is not callable
    # print(type(musketyr1))
    # print(type(musketyr2))
    # print(type(musketyr3))
    # print(type(musketyr4))
    #
    # print(type(carodej1))
    # print(type(carodej2))
    # print(type(carodej3))
    # print(type(carodej4))

    # podle tohohle pak můžeš nadefinovat klávesy nahoru, dolu, atd...
    # if event.key == pygame.K_UP:
            #     # Provádět akce pro stisknutí klávesy UP
            #     print("Klávesa UP byla stisknuta")
            # elif event.key == pygame.K_DOWN:
            #     # Provádět akce pro stisknutí klávesy DOWN
            #     print("Klávesa DOWN byla stisknuta")
            # elif event.key == pygame.K_LEFT:
            #     # Provádět akce pro stisknutí klávesy LEFT
            #     print("Klávesa LEFT byla stisknuta")
            # elif event.key == pygame.K_RIGHT:
            #     # Provádět akce pro stisknutí klávesy RIGHT
            #     print("Klávesa RIGHT byla stisknuta")
            #     pass


def musketyr_vyber_a():
    return musketyr_vyber_a

def carodej_vyber(carodej_vyber):
    return carodej_vyber