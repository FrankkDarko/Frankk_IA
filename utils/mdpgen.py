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
          ">>>>[1] Faible   : 6 carractére aléatoire\n"
          ">>>>[2] Moyen    : 8 carractére aléatoire\n"
          ">>>>[3] Fort     : 16 carractére aléatoire\n"
          ">>>>[4] Military : 32 carractére aléatoire\n"
          ">>>>[5] Perso    : vous définisser chaque paramètre\n"
          ">>>>[6] Phrase   : modifie une phrase de votre choix\n"
          "")

    choix = input("IA > Merci de faire votre choix : ").lower()

    if choix == "faible" or "1":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 6)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    if choix == "moyen" or "2":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 8)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    if choix == "fort" or "3":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 16)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    if choix == "military" or "4":
        print("----------- Les résultats -----------")
        for c in range(6):
            temp = random.sample(all, 32)
            password = "".join(temp)
            print(Fore.YELLOW + "[" + str(c) + "]" + Style.RESET_ALL + Fore.BLUE + " Mots de passe aléatoire de niveau "
                  + Style.BRIGHT + choix + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                  + password + Style.RESET_ALL)

    if choix == "perso" or "5":

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

    if choix == "phrase" or "6":
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



generator()
