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

    print(Style.RESET_ALL + Fore.GREEN +
          "Génerateur de mots de passe\n"
          "Choix :\n"
          + Fore.YELLOW +
          Fore.RED + "─► [1] Faible   : " + Fore.YELLOW + "6 carractére aléatoire\n" +
          Fore.RED + "─► [2] Moyen    : " + Fore.YELLOW + "8 carractére aléatoire\n" +
          Fore.RED + "─► [3] Fort     : " + Fore.YELLOW + "16 carractére aléatoire\n" +
          Fore.RED + "─► [4] Military : " + Fore.YELLOW + "32 carractére aléatoire\n" +
          Fore.RED + "─► [5] Perso    : " + Fore.YELLOW + "vous définisser chaque paramètre\n" +
          Fore.RED + "─► [6] Phrase   : " + Fore.YELLOW + "modifie une phrase de votre choix\n" +
          "" + Style.RESET_ALL)

    choix = input(Fore.RED + Style.BRIGHT + "IA >" + Fore.LIGHTYELLOW_EX + " Merci de faire votre choix : "
                  + Fore.LIGHTCYAN_EX).lower()

    if choix == "faible":
        print(Fore.RED + Style.BRIGHT + "----------- Les résultats -----------" + Style.RESET_ALL)
        for c in range(6):
            temp = random.sample(all, 6)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    elif choix == "moyen":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 8)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    elif choix == "fort":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 16)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    elif choix == "military":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 32)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    elif choix == "perso":

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

    elif choix == "phrase":
        phrase = input("donner moi une phrase : ")

        changement = input("Donner le nombre de changement voulut : ")

        plist = list(phrase.replace(" ", "").lower())

        lenplist = len(plist)

        for c in range(6):

            for i in range(int(changement)):
                change_choice = random.randint(0, lenplist - 1)
                temp = random.choice(NUM)
                temp2 = random.choice(CAR)

                tp = [temp, temp2]

                plist[change_choice] = random.choice(tp)

            phrase_fin = "".join(plist)

            print(Fore.YELLOW + "[" + str(
                c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                + phrase_fin + Style.RESET_ALL)

