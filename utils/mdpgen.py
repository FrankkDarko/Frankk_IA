import random
import string
from colorama import Fore
from colorama import Style


def generator():
    MIN = string.ascii_lowercase
    MAJ = string.ascii_uppercase
    NUM = string.digits
    CAR = string.punctuation

    all = MIN + MAJ + NUM + CAR

    print("Génerateur de mots de passe\n"
          "Choix :\n"
          ">>>> Faible  : 6 carractére aléatoire\n"
          ">>>> Moyen   : 8 carractére aléatoire\n"
          ">>>> Fort    : 16 carractére aléatoire\n"
          ">>>> Military: 32 carractére aléatoire\n"
          ">>>> Perso   : vous définisser chaque paramètre\n"
          "")

    choix = input("IA > Merci de faire votre choix : ").lower()

    if choix == "faible":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 6)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    if choix == "moyen":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 8)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    if choix == "fort":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 16)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    if choix == "military":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 32)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    if choix == "perso":

        try:
            lettre_MAJ = input("Le nombre de lettre majuscule : ")
            lettre_MIN = input("Le nombre de lettre minuscule : ")
            nombre_NUM = input("Le nombre de chiffre : ")
            nombre_CAR = input("Le nombre de carractére spéciaux : ")
            tot = int(lettre_MAJ) + int(lettre_MIN) + int(nombre_NUM) + int(nombre_CAR)
            print("Nombre total de carractéres : " + str(tot))
            print("----------- Les résultats -----------")
            for c in range(6):
                temp = random.sample(MIN, int(lettre_MIN))
                temp2 = random.sample(MAJ, int(lettre_MAJ))
                temp3 = random.sample(NUM, int(nombre_NUM))
                temp4 = random.sample(CAR, int(nombre_CAR))
                all_temp = temp + temp2 + temp3 + temp4
                rand_temp = random.sample(all_temp, int(tot))
                password = "".join(rand_temp)
                print(Fore.YELLOW + "[" + str(
                    c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                      + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                      + password + Style.RESET_ALL)
        except ValueError:
            print("Les valeurs entrée sont incorrecte !")

