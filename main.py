#!/usr/bin/env python3
# coding:utf-8

""" Import des librairies """
import random
import pandas as pd
import csv
from utils import pfc, eightball, mdpgen, search, cryptor, randomme
from knowledge import words, help, infofkia, sentiments
from colorama import Fore
from colorama import Style

# entrée dans le programme
print(Fore.YELLOW + "Bienvenue dans Frankk IA votre nouvelle ami !\n" + Style.RESET_ALL)
print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Qui es tu ? ")
user = input(Fore.GREEN + "Utilisateur > " + Fore.LIGHTCYAN_EX)  # prise du nom de l'utilisateur

# Variable
Bonjour = words.Bonjour
Commandes = words.Commandes
Amabilite = words.Amabilite
JeNeSuisPasUnRobot = words.JeNeSuisPasUnRobot
Humour = words.Humour
ProfilIA = words.ProfilIA
exit_programme = False
fund = False
enter_user = Fore.GREEN + Style.BRIGHT + user + " > " + Fore.LIGHTCYAN_EX
rep_bot = Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX

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

        enter = input(enter_user).lower()
        fund = False

        for i in range(len(Commandes.commandes)):
            if enter == Commandes.commandes[10]:  # Affiche la commande [info]
                infofkia.info_of_fkia()
                fund = True
                break

            if enter == Commandes.commandes[0] \
                    or enter == Commandes.alias[0]:  # Générateur de mots de passes [mdpgen]
                print(rep_bot + "Je vous lance le programme générateur de mots de passe")
                mdpgen.generator()
                fund = True
                break

            if enter == Commandes.commandes[1] or enter == Commandes.alias[1]:  # pour jouer au 8ball [8ball]
                eightball.oracle()
                fund = True
                break

            if enter == Commandes.commandes[2] or enter == Commandes.alias[3]:  # pour faire des recherches
                search.search()
                fund = True
                break

            if enter == Commandes.commandes[3] \
                    or enter == Commandes.alias[2]:  # Commande pierre papier ciseaux [pfc]
                print(rep_bot + "Lancement du pierre feuille ciseaux")
                pfc.ppc()
                fund = True
                break

            if enter == Commandes.commandes[8] or enter == Commandes.commandes[9]:  # Commande Help [help] ou [aide]
                help.help_me()
                fund = True
                break

            if enter == Commandes.commandes[11] \
                    or enter == Commandes.commandes[12]:  # Affiche la commande [cryptor]
                cryptor.cryptor()
                fund = True
                break

            if enter == Commandes.commandes[13] \
                    or enter == Commandes.commandes[14]:  # Affiche la commande [randomme]
                randomme.randomme()
                fund = True
                break

            if enter == Commandes.commandes[5] \
                    or enter == Commandes.commandes[6]:  # Sortie du programe [sortie] [exit]
                print(rep_bot + "Bye et à bientôt !")
                exit_programme = True
                fund = True
                break

        for i in range(len(Bonjour.demande)):

            if enter == Bonjour.demande[i]:  # Salutation
                random_rep_bonjour = random.randint(0, len(Bonjour.reponse) - 1)
                print(rep_bot + Bonjour.reponse[random_rep_bonjour])
                fund = True
                break

        for i in range(len(Amabilite.demande)):

            if enter == Amabilite.demande[i]:  # répond à "ça va ?"
                sentiments.iasentiments()
                print(rep_bot + "et toi ?")
                enter = input(enter_user).lower()
                for e in range(len(Amabilite.rep_hum_good)):
                    if enter == Amabilite.rep_hum_good[e]:
                        random_rep_good = random.randint(0, len(Amabilite.reponse_good) - 1)
                        print(rep_bot + Amabilite.reponse_good[random_rep_good])
                        fund = True
                        break
                for f in range(len(Amabilite.rep_hum_bad)):
                    if enter == Amabilite.rep_hum_bad[f]:
                        random_rep_bad = random.randint(0, len(Amabilite.reponse_bad) - 1)
                        print(rep_bot + Amabilite.reponse_bad[random_rep_bad])
                        fund = True
                        break

        for i in range(len(JeNeSuisPasUnRobot.demande)):

            if enter == JeNeSuisPasUnRobot.demande[i]:  # car ce n'est pas un robot !
                random_rep_JNSPUR = random.randint(0, len(JeNeSuisPasUnRobot.reponse) - 1)
                print(rep_bot + JeNeSuisPasUnRobot.reponse[random_rep_JNSPUR])
                enter = input(enter_user).lower()
                if enter == JeNeSuisPasUnRobot.rep_hum[0]:
                    print(rep_bot + JeNeSuisPasUnRobot.rep_bot[1])
                    fund = True
                    break
                if enter == JeNeSuisPasUnRobot.rep_hum[1] or enter == JeNeSuisPasUnRobot.rep_hum[2]:
                    print(rep_bot + JeNeSuisPasUnRobot.rep_bot[0])
                    fund = True
                    break

        for i in range(len(Humour.commandes)):

            if enter == Humour.commandes[i]:  # Lance des blague
                randomme.faituneblague()
                fund = True
                break

        for i in range(len(ProfilIA.q_nom)):

            if enter == ProfilIA.q_nom[i]:  # Donne son nom
                random_rep_ProfilIA = random.randint(0, len(ProfilIA.r_nom) - 1)
                print(rep_bot + ProfilIA.r_nom[random_rep_ProfilIA])
                fund = True
                break

        for i in range(len(ProfilIA.q_age)):

            if enter == ProfilIA.q_age[i]:  # Donne l'âge
                infofkia.ageIA()
                fund = True
                break

        for i in range(len(ProfilIA.q_age)):

            if enter == ProfilIA.q_sentiments[i]:  # Demande si il a des sentiments
                random_rep_SENTIMENTS = random.randint(0, len(ProfilIA.r_sentiments) - 1)
                print(rep_bot + ProfilIA.r_sentiments[random_rep_SENTIMENTS])
                fund = True
                break

        if not fund:
            print(rep_bot + "Je n'es pas compris votre message, merci de recommencé")
