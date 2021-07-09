import random
from colorama import Fore
from colorama import Style

enter = ""
score_joueur = 0
score_ordi = 0


def ppc():
    global enter, score_joueur, score_ordi
    continuer = True
    while continuer:
        affiche_score = Fore.BLUE + "\nScore joueur : " + Fore.GREEN + str(score_joueur) + Fore.MAGENTA + \
                        "\nScore ordinateur : " + Fore.GREEN + str(score_ordi) + "\n" + Style.RESET_ALL
        print(affiche_score)
        print(Fore.YELLOW + Style.BRIGHT + "Bienvenue dans ce Pierre Feuille Ciseaux, les régle sont celle connu de "
                                           "tous.\nMerci de choisir : pierre, feuille, ciseaux ou sortir"
              + Style.RESET_ALL)
        enter_verif = False
        while not enter_verif:
            enter = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Votre choix : " + Style.RESET_ALL).lower()
            if enter == "pierre" or enter == "feuille" or enter == "ciseaux":
                enter_verif = True
            elif enter == "sortir":
                print(Fore.YELLOW + Style.BRIGHT + "\n\nMerci d'avoir jouer, Le socre finale est : " + affiche_score
                      + Style.RESET_ALL)
                continuer = False
                break
            else:
                print(Fore.RED + Style.BRIGHT + "Mauvaise entrée" + Style.RESET_ALL)

        pierre = random.randint(1, 100)
        feuille = random.randint(1, 100)
        ciseaux = random.randint(1, 100)
        #  print("P : " + str(pierre) + " F : " + str(feuille) + " C : " + str(ciseaux))
        possibilite = ["Pierre", "Feuille", "Ciseaux"]
        choix_it = random.choices(possibilite, weights=[pierre, feuille, ciseaux], k=1)
        choix = choix_it[0]
        victoire = Fore.GREEN + Style.BRIGHT + "\nVictoire du joueur" + Style.RESET_ALL
        defaite = Fore.RED + Style.BRIGHT + "\nDefaite du joueur" + Style.RESET_ALL
        egaliter = Fore.YELLOW + Style.BRIGHT + "\nPersonne ne gagne" + Style.RESET_ALL

        if enter == "pierre" and choix == "Ciseaux":
            score_joueur = score_joueur + 1
            print(enter + "\n" + choix + victoire + "\n")
        elif enter == "pierre" and choix == "Feuille":
            score_ordi = score_ordi + 1
            print(enter + "\n" + choix + defaite)
        elif enter == "pierre" and choix == "Pierre":
            print(enter + "\n" + choix + egaliter)

        elif enter == "feuille" and choix == "Ciseaux":
            score_ordi = score_ordi + 1
            print(enter + "\n" + choix + defaite)
        elif enter == "feuille" and choix == "Feuille":
            print(enter + "\n" + choix + egaliter)
        elif enter == "feuille" and choix == "Pierre":
            score_joueur = score_joueur + 1
            print(enter + "\n" + choix + victoire)

        elif enter == "ciseaux" and choix == "Ciseaux":
            print(enter + "\n" + choix + egaliter)
        elif enter == "ciseaux" and choix == "Feuille":
            score_joueur = score_joueur + 1
            print(enter + "\n" + choix + victoire)
        elif enter == "ciseaux" and choix == "Pierre":
            score_ordi = score_ordi + 1
            print(enter + "\n" + choix + defaite)


"""
Possible amilioration :
faire differente variable definissant les victoire defaite et egalité puis faire une boucle pour 
verifier dans qu'elle situation ont es
"""
