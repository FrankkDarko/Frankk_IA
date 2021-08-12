#!/usr/bin/env python3
# coding:utf-8


""" Import des librairies """
import random
import pandas as pd
import csv
from utils import pfc, eightball, mdpgen, search, cryptor, randomme
from knowledge import words, help, infofkia, sentiments
from connexion import *
from colorama import Fore
from colorama import Style
import tkinter
from tkinter import ttk
from ttkthemes import ThemedTk

# Variable
user_fund = False
user = str(Utilisateur.get())
Bonjour = words.Bonjour
Commandes = words.Commandes
Amabilite = words.Amabilite
JeNeSuisPasUnRobot = words.JeNeSuisPasUnRobot
Humour = words.Humour
ProfilIA = words.ProfilIA
exit_programme = False
fund = False
enter_user = user + " > "
rep_bot = "IA > "


def discussion():
    enter = EntryMessage.get().lower()
    print(enter_user + enter)
    EntryMessage.set("")
    t['state'] = 'normal'
    t.insert('end', enter_user, 'usr')
    t.insert('end', enter + "\n")

    fund_words = False

    for i in range(len(Commandes.commandes)):
        if enter == Commandes.commandes[10]:  # Affiche la commande [info]

            msg = f'Cette option est en cours de development en mode graphique'
            showinfo(title='Erreur', message=msg)

            fund_words = True
            break

        if enter == Commandes.commandes[0] \
                or enter == Commandes.alias[0]:  # Générateur de mots de passes [mdpgen]
            mdpgen.gui_mdpgen()
            fund_words = True
            break

        if enter == Commandes.commandes[1] or enter == Commandes.alias[1]:  # pour jouer au 8ball [8ball]

            msg = f'Cette option est en cours de development en mode graphique'
            showinfo(title='Erreur', message=msg)

            fund_words = True
            break

        if enter == Commandes.commandes[2] or enter == Commandes.alias[3]:  # pour faire des recherches

            msg = f'Cette option est en cours de development en mode graphique'
            showinfo(title='Erreur', message=msg)

            fund_words = True
            break

        if enter == Commandes.commandes[3] \
                or enter == Commandes.alias[2]:  # Commande pierre papier ciseaux [pfc]

            msg = f'Cette option est en cours de development en mode graphique'
            showinfo(title='Erreur', message=msg)

            fund_words = True
            break

        if enter == Commandes.commandes[8] or enter == Commandes.commandes[9]:  # Commande Help [help] ou [aide]
            t.insert('end', rep_bot, 'ia')
            t.insert('end', "Voici les commandes disponible :" + "\n")

            with open("knowledge/info_help.csv", newline='') as f:
                lire = pd.read_csv(f)
                nom_value = lire["nom"].values
                alias_value = lire["alias"].values
                desc_value = lire["description"].values

                for i in range(len(lire)):
                    t.insert('end', "\nCommande : ", 'gris')
                    t.insert('end', nom_value[i], 'rouge')
                    t.insert('end', "\n             └► " + "Alias : ", 'gris')
                    t.insert('end', "[" + alias_value[i] + "]", 'rouge')
                    t.insert('end', "  ||  Description : ", 'gris')
                    t.insert('end', desc_value[i] + "\n", 'orange')
            fund_words = True
            t['state'] = 'disabled'
            break

        if enter == Commandes.commandes[11] \
                or enter == Commandes.commandes[12]:  # Affiche la commande [cryptor]

            msg = f'Cette option est en cours de development en mode graphique'
            showinfo(title='Erreur', message=msg)

            fund_words = True
            break

        if enter == Commandes.commandes[13] \
                or enter == Commandes.commandes[14]:  # Affiche la commande [randomme]

            msg = f'Cette option est en cours de development en mode graphique'
            showinfo(title='Erreur', message=msg)

            fund_words = True
            break

        if enter == Commandes.commandes[5] \
                or enter == Commandes.commandes[6]:  # Sortie du programe [sortie] [exit]
            print(rep_bot + "Bye et à bientôt !")
            fund_words = True
            fenetre.destroy()
            break

    for i in range(len(Bonjour.demande)):

        if enter == Bonjour.demande[i]:  # Salutation
            random_rep_bonjour = random.randint(0, len(Bonjour.reponse) - 1)
            t.insert('end', rep_bot, 'ia')
            t.insert('end', Bonjour.reponse[random_rep_bonjour] + "\n")
            t['state'] = 'disabled'
            print(rep_bot + Bonjour.reponse[random_rep_bonjour])
            fund_words = True
            break

    for i in range(len(Amabilite.demande)):

        if enter == Amabilite.demande[i]:  # répond à "ça va ?"
            sentiments.iasentiments()
            t.insert('end', rep_bot, 'ia')
            t.insert('end', sentiments.iasentiments() + "\n")
            print(rep_bot + "et toi ?")
            t.insert('end', rep_bot, 'ia')
            t.insert('end', "et toi ?" + "\n")
            t['state'] = 'disabled'

    for i in range(len(Amabilite.rep_hum_good)):
        if enter == Amabilite.rep_hum_good[i]:
            random_rep_good = random.randint(0, len(Amabilite.reponse_good) - 1)
            t.insert('end', rep_bot, 'ia')
            t.insert('end', Amabilite.reponse_good[random_rep_good] + "\n")
            t['state'] = 'disabled'
            print(rep_bot + Amabilite.reponse_good[random_rep_good])
            fund_words = True
            break

    for i in range(len(Amabilite.rep_hum_bad)):
        if enter == Amabilite.rep_hum_bad[i]:
            random_rep_bad = random.randint(0, len(Amabilite.reponse_bad) - 1)
            t.insert('end', rep_bot, 'ia')
            t.insert('end', Amabilite.reponse_bad[random_rep_bad] + "\n")
            t['state'] = 'disabled'
            print(rep_bot + Amabilite.reponse_bad[random_rep_bad])
            fund_words = True
            break

    for i in range(len(JeNeSuisPasUnRobot.demande)):

        if enter == JeNeSuisPasUnRobot.demande[i]:  # car ce n'est pas un robot !
            random_rep_JNSPUR = random.randint(0, len(JeNeSuisPasUnRobot.reponse) - 1)
            print(rep_bot + JeNeSuisPasUnRobot.reponse[random_rep_JNSPUR])
            t.insert('end', rep_bot, 'ia')
            t.insert('end', JeNeSuisPasUnRobot.reponse[random_rep_JNSPUR] + "\n")
            t['state'] = 'disabled'
            enter = input(enter_user).lower()

            if enter == JeNeSuisPasUnRobot.rep_hum[0]:
                print(rep_bot + JeNeSuisPasUnRobot.rep_bot[1])
                t.insert('end', rep_bot, 'ia')
                t.insert('end', JeNeSuisPasUnRobot.rep_bot[1] + "\n")
                t['state'] = 'disabled'
                fund_words = True
                break

            if enter == JeNeSuisPasUnRobot.rep_hum[1] or enter == JeNeSuisPasUnRobot.rep_hum[2]:
                print(rep_bot + JeNeSuisPasUnRobot.rep_bot[0])
                t.insert('end', rep_bot, 'ia')
                t.insert('end', JeNeSuisPasUnRobot.rep_bot[0] + "\n")
                t['state'] = 'disabled'
                fund_words = True
                break

    for i in range(len(Humour.commandes)):

        if enter == Humour.commandes[i]:  # Lance des blague
            randomme.faituneblague()
            t.insert('end', randomme.faituneblague() + "\n")
            t['state'] = 'disabled'
            fund_words = True
            break

    for i in range(len(ProfilIA.q_nom)):

        if enter == ProfilIA.q_nom[i]:  # Donne son nom
            random_rep_ProfilIA = random.randint(0, len(ProfilIA.r_nom) - 1)
            print(rep_bot + ProfilIA.r_nom[random_rep_ProfilIA])
            t.insert('end', rep_bot, 'ia')
            t.insert('end', ProfilIA.r_nom[random_rep_ProfilIA] + "\n")
            t['state'] = 'disabled'
            fund_words = True
            break

    for i in range(len(ProfilIA.q_age)):

        if enter == ProfilIA.q_age[i]:  # Donne l'âge
            infofkia.ageIA()
            t.insert('end', rep_bot, 'ia')
            t.insert('end', infofkia.ageIA() + "\n")
            t['state'] = 'disabled'
            fund_words = True
            break

    for i in range(len(ProfilIA.q_age)):

        if enter == ProfilIA.q_sentiments[i]:  # Demande si il a des sentiments
            random_rep_SENTIMENTS = random.randint(0, len(ProfilIA.r_sentiments) - 1)
            print(rep_bot + ProfilIA.r_sentiments[random_rep_SENTIMENTS])
            t.insert('end', rep_bot, 'ia')
            t.insert('end', ProfilIA.r_sentiments[random_rep_SENTIMENTS] + "\n")
            t['state'] = 'disabled'
            fund_words = True
            break

    if not fund_words:
        print(rep_bot + "Je n'es pas compris votre message, merci de recommencé")
        t.insert('end', rep_bot, 'ia')
        t.insert('end', "Je n'es pas compris votre message, merci de recommencé" + "\n")
        t['state'] = 'disabled'


# Création d'une fenêtre avec la classe Tk :
# fenetre = tkinter.Tk()
fenetre = ThemedTk(theme="arc")


# Ajout d'un titre à la fenêtre principale :
fenetre.title("Frankk IA")

# Définir un icone :
fenetre.call('wm', 'iconphoto', fenetre._w, tkinter.PhotoImage(file='img/logo.png'))

# Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
fenetre.config(bg="#979797")

# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("640x480")

# Configuration du gestionnaire de grille
fenetre.rowconfigure(0, weight=1)
fenetre.columnconfigure(0, weight=1)

# Bouton envoie
bouton_send = ttk.Button(fenetre, text="Envoie", command=discussion)
fenetre.bind('<Return>', lambda b: bouton_send.invoke())
bouton_send.grid(row=1, column=1, sticky="nsew")

# Entrée utilisateur
EntryMessage = tkinter.StringVar()
Champ = ttk.Entry(fenetre, textvariable=EntryMessage)
Champ.focus_set()
Champ.grid(row=1, column=0, sticky="nsew")

# Affichage du texte
t = Text(fenetre, width=40, height=10)
t.tag_configure('gris', foreground='#757575')
t.tag_configure('ia', foreground='#FF0000')
t.tag_configure('usr', foreground='#32EA7A')
t.tag_configure('orange', foreground='#F3B017')
t.tag_configure('rouge', foreground='#F73100')
t.insert("end", "Bienvenue dans Frankk IA votre nouvelle ami !\n\n", 'gris')
t.grid(row=0, column=0, columnspan=2, rowspan=1, sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

if user == "Frankk":
    t.insert('end', rep_bot, 'ia')
    t.insert('end', "Bienvenue mon créateur" + "\n")
else:
    t.insert('end', rep_bot, 'ia')
    t.insert('end', "Bonjour " + user + "\n")
t['state'] = 'disabled'

# Affichage de la fenêtre créée :
fenetre.mainloop()
