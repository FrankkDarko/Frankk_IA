import random
import string
from tkinter.ttk import Combobox

from colorama import Fore
from colorama import Style
import tkinter
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo


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


def gui_mdpgen():
    def generateur(event):
        r['state'] = 'normal'
        option = Champ.get()

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

        if option == "faible":
            r.insert("end", "\n-------------------------------- Les résultats --------------------------------\n\n",
                     'rouge')
            for c in range(6):
                temp = random.sample(all, 6)
                password = "".join(temp)
                r.insert("end", "[" + str(c) + "]", 'orange')
                r.insert("end", " Mots de passe aléatoire de niveau " + option + " : ", 'gris')
                r.insert("end", password + "\n", 'vert')
            r['state'] = 'disabled'

        elif option == "moyen":
            r.insert("end", "\n-------------------------------- Les résultats --------------------------------\n\n",
                     'rouge')
            for c in range(6):
                temp = random.sample(all, 8)
                password = "".join(temp)
                r.insert("end", "[" + str(c) + "]", 'orange')
                r.insert("end", " Mots de passe aléatoire de niveau " + option + " : ", 'gris')
                r.insert("end", password + "\n", 'vert')
            r['state'] = 'disabled'

        elif option == "fort":
            print("----------- Les résultats -----------")
            r.insert("end", "\n-------------------------------- Les résultats --------------------------------\n\n",
                     'rouge')
            for c in range(6):
                temp = random.sample(all, 16)
                password = "".join(temp)
                r.insert("end", "[" + str(c) + "]", 'orange')
                r.insert("end", " Mots de passe aléatoire de niveau " + option + " : ", 'gris')
                r.insert("end", password + "\n", 'vert')
            r['state'] = 'disabled'

        elif option == "military":
            r.insert("end", "\n-------------------------------- Les résultats --------------------------------\n\n",
                     'rouge')
            for c in range(6):
                temp = random.sample(all, 32)
                password = "".join(temp)
                r.insert("end", "[" + str(c) + "]", 'orange')
                r.insert("end", " Mots de passe aléatoire de niveau " + option + " : ", 'gris')
                r.insert("end", password + "\n", 'vert')
            r['state'] = 'disabled'

        elif option == "perso":
            msg = f'Cette option est en cours de development en mode graphique'
            showinfo(title='Erreur', message=msg)

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
                          + Style.BRIGHT + option + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                          + password + Style.RESET_ALL)
            except ValueError:
                print("Les valeurs entrée sont incorrecte !")

        elif option == "phrase":
            msg = f'Cette option est en cours de development en mode graphique'
            showinfo(title='Erreur', message=msg)

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
                      + Style.BRIGHT + option + " : " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
                      + phrase_fin + Style.RESET_ALL)

    # Création d'une fenêtre avec la classe Tk :
    gui_mdp = ThemedTk(theme="arc")

    # Ajout d'un titre à la fenêtre principale :
    gui_mdp.title("Frankk IA ~ Générateur de mots de passe")

    # Définir un icone :
    # gui_mdp.call('wm', 'iconphoto', gui_mdp._w, tkinter.PhotoImage(file='/img/logo.png'))

    # Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
    # gui_mdp.config(bg="#979797")

    # Définir les dimensions par défaut la fenêtre principale :
    gui_mdp.geometry("640x480")
    gui_mdp.maxsize(640, 480)
    gui_mdp.columnconfigure(0, weight=1)
    gui_mdp.rowconfigure(0, weight=1)

    # Entrée utilisateur
    EntryChoice = tkinter.StringVar()
    Champ = Combobox(gui_mdp, textvariable=EntryChoice)
    Champ['value'] = ('faible', 'moyen', 'fort', 'military', 'perso', 'phrase')
    Champ.state(["readonly"])
    Champ.grid(row=0, column=3, sticky="new", pady=10, padx=5)
    Champ.bind('<<ComboboxSelected>>', generateur)

    # Label
    label = tkinter.Label(gui_mdp, text="Choix")
    label.grid(row=0, column=1, columnspan=1, sticky="ne",  pady=15, padx=5)

    # Affichage du texte
    r = tkinter.Text(gui_mdp, width=40, height=25)
    r.tag_configure('gris', foreground='#757575')
    r.tag_configure('orange', foreground='#F3B017')
    r.tag_configure('vert', foreground='#17F353')
    r.tag_configure('rouge', foreground='#F31717')
    r.insert("end", "Bienvenue dans le générateur de mots de passe !\n\n\n", 'gris')
    r.grid(row=1, column=0, rowspan=4, columnspan=4, sticky="nesw")
    r['state'] = 'disabled'

    # Affichage de la fenêtre créée :
    gui_mdp.mainloop()
