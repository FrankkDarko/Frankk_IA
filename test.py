#!/usr/bin/env python3
# coding:utf-8
import json
""" Import des librairies"""
"""
from utils import pfc, eightball, mdpgen, search
from knowledge import words, help
import random
from colorama import Fore
from colorama import Style

version = "FKIA_Testing"  # Versions de Frankk IA

# entrée dans le programme
print(Fore.YELLOW + "Bienvenue dans Frankk IA votre nouvelle ami !\n" + Style.RESET_ALL)
print("IA > Qui es tu ? ")
user = input("Utilisateur > ")  # prise du nom de l'utilisateur

# Variable
Bonjour = words.Bonjour
Commandes = words.Commandes
Amabilite = words.Amabilite
JeNeSuisPasUnRobot = words.JeNeSuisPasUnRobot
exit_programme = False
enter_user = user + " > "
rep_bot = "IA > "


# début de la boucle globale de l'IA
while not exit_programme:
    fichier_users = open("knowledge/users.txt", "rt")
    list_users = fichier_users.read()
    #  print(list_users)
    fichier_users.close()

    write_users = open("knowledge/users.txt", "at")
    if user in list_users:
        if user == "Frankk":
            print(rep_bot + "Bienvenue mon créateur")
        else:
            print(rep_bot + "Re bonjour " + user)
    else:
        write_users.write(user + ",")
        print(rep_bot + "Enchanté " + user)
        print(rep_bot + "Je vous ajoute dans ma liste")
    write_users.close()

    print(rep_bot + "Ont fait quoi maintenant ?")

    while not exit_programme:
        try:
            enter = input(enter_user)
            enter_low = enter.lower()
            #  enter_split = enter.lower().split(" ")
            if enter_low == Commandes.commandes[5] or enter_low == Commandes.commandes[6]:  # Sortie du programe
                exit_programme = True
                break

            for i in range(len(enter.lower().split(" "))):
                random_rep_bonjour = random.randint(0, len(Bonjour.reponse) - 1)
                if enter_low == Bonjour.demande[i]:  # Salutation
                    print(rep_bot + Bonjour.reponse[random_rep_bonjour])
                    break

            else:  # entrer non comprise
                print(rep_bot + "J'ai rien compris !")
        except IndexError:
            print(rep_bot + "Je n'est pas pus vérifier cette information, merci de recommencé")



        elif enter_split[0] in word:  # Discution classique
            if enter_split[0] == word[0]:
                print(rep_bot + "Salut " + user + " !")
            elif enter_split[0] == word[1] and enter_split[1] == word[2]:
                print(rep_bot + "Bien et toi ?")
            elif enter_split[0] == word[4]:
                print(rep_bot + "Super !")

        elif enter_split[0] in commandes:  # Commande actif
            print(rep_bot + "cmd found")

"""

d = "sortie"
d2 = "exit"

with open("knowledge/words.json") as jsonFile:
    words_load = json.load(jsonFile)
    for words in words_load["words"]:

        demandes = words["demande"]
        print(demandes)
        reponses = words["response"]
        print(reponses)
        if d == demandes[5]:
            print(reponses[0])
        if d2 == demandes[6]:
            print(reponses[0])



