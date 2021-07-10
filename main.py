#!/usr/bin/env python3
# coding:utf-8

""" Import des librairies """
import random
import pandas as pd
import csv
from utils import pfc, eightball, mdpgen, search
from knowledge import words, help, infofkia
from colorama import Fore
from colorama import Style


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
    with open('knowledge/users.csv', newline='') as f:  # Ouverture du fichier CSV
        utilisateur = []
        lire = pd.read_csv("knowledge/users.csv")  # chargement des lignes du fichier csv
        users_list = lire["Pseudo"].values  # Récuperation de tous les pseudo déjà sauvegarder
        if user in users_list:  # Voir si l'utilisateur et déjà dans la liste
            if user == "Frankk":
                print(rep_bot + "Bienvenue mon créateur")
            else:
                print(rep_bot + "Re bonjour " + user)
        else:  # Si l'utilisateur n'est pas enregistrer
            print(rep_bot + "Enchanté " + user)
            print(rep_bot + "Je vais vous poser une ou deux questions si vous voulez bien sinon laisser vide")
            print(rep_bot + "Votre âge ?")
            age = input(enter_user)
            if age == "" or age.isdigit() is False:
                age = "none"
            print(rep_bot + "Votre prénom ?")
            prenom = input(enter_user)
            if prenom == "":
                prenom = "none"
            print(rep_bot + "Votre nom ?")
            nom = input(enter_user)
            if nom == "":
                nom = "none"
            print(rep_bot + "Je vous ajoute dans ma liste")
            with open('knowledge/users.csv', 'a',
                      newline='') as users_file:  # Ajout d'une ligne dans le fichier csv
                ecrire = csv.writer(users_file)  # préparation à l'écriture
                ecrire.writerow([user, age, prenom, nom])  # Mettre dans écrire cette nouvelle ligne

    print(rep_bot + "Ont fait quoi maintenant ?")

    while not exit_programme:
        try:
            enter = input(enter_user).lower()
            if enter == Commandes.commandes[5] or enter == Commandes.commandes[6]:  # Sortie du programe [sortie] [exit]
                exit_programme = True
                break
            if enter == Commandes.commandes[10]:
                infofkia.info_of_fkia()

            for i in range(len(enter.lower().split(" "))):
                random_rep_bonjour = random.randint(0, len(Bonjour.reponse) - 1)
                if enter == Bonjour.demande[i]:  # Salutation
                    print(rep_bot + Bonjour.reponse[random_rep_bonjour])
                    break
                if enter == Amabilite.demande[0] or enter == Amabilite.demande[1] or enter == Amabilite.demande[2]:  # répond à "ça va ?"
                    print(rep_bot + Amabilite.reponse[0])
                    enter = input(enter_user)
                    enter = enter.lower()
                    if enter == Amabilite.demande[3] or enter == Amabilite.demande[4]:
                        print(rep_bot + Amabilite.reponse[1])
                        break
                    if enter == Amabilite.demande[5] or enter == Amabilite.demande[6]:
                        print(rep_bot + Amabilite.reponse[2])
                        break
                if enter == JeNeSuisPasUnRobot.demande[i]:  # car ce n'est pas un robot !
                    random_rep_JNSPUR = random.randint(0, len(JeNeSuisPasUnRobot.reponse) - 1)
                    print(rep_bot + JeNeSuisPasUnRobot.reponse[random_rep_JNSPUR])
                    break

                if enter == Commandes.commandes[0] or enter == Commandes.alias[0]:  # Générateur de mots de passes [mdpgen]
                    print(rep_bot + "Je vous lance le programme générateur de mots de passe")
                    mdpgen.generator()
                    break
                if enter == Commandes.commandes[1] or enter == Commandes.alias[1]:  # pour jouer au 8ball [8ball]
                    eightball.oracle()
                    break
                if enter == Commandes.commandes[2] or enter == Commandes.alias[3]:  # pour faire des recherches
                    search.search()
                    break
                if enter == Commandes.commandes[3] or enter == Commandes.alias[2]:  # Commande pierre papier ciseaux [pfc]
                    print(rep_bot + "Lancement du pierre feuille ciseaux")
                    pfc.ppc()
                    break
                if enter == Commandes.commandes[8] or enter == Commandes.commandes[9]:  # Commande Help [help] ou [aide]
                    help.help_me()
                    break

            else:  # entrer non comprise
                print(rep_bot + "J'ai rien compris !")
        except IndexError:
            print(rep_bot + "Je n'est pas pus vérifier cette information, merci de recommencé")

"""

"""
