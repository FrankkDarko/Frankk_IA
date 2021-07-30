# !/usr/bin/env python3
# coding:utf-8
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter.messagebox import *  # boîte de dialogue
import pandas as pd

with open('knowledge/users.csv', newline='') as f:  # Ouverture du fichier CSV
    lire = pd.read_csv("knowledge/users.csv")  # chargement des lignes du fichier csv
    users_list = lire["Pseudo"].values  # Récuperation de tous les pseudo déjà sauvegarder


def verification():
    if Utilisateur.get() in users_list:
        connect.destroy()
    else:
        showwarning('Information', 'utilisateur incorrect.\nVeuillez recommencer !')


# Création de la fenêtre principale (main window)
connect = ThemedTk(theme="arc")
connect.title('Identification requise')
connect.call('wm', 'iconphoto', connect._w, PhotoImage(file='img/logo.png'))

# Création d'un widget Label (texte 'Utilisateur')
Label1 = Label(connect, text='Utilisateur ')
Label1.pack(side=LEFT, padx=5, pady=5)

# Création d'un widget Entry (champ de saisie utilisateur)
Utilisateur = StringVar()
Champ = ttk.Entry(connect, textvariable=Utilisateur)
Champ.focus_set()
Champ.pack(side=LEFT, padx=5, pady=5)

# Création d'un widget Button (bouton Valider)
Bouton = ttk.Button(connect, text='Valider', command=verification)
connect.bind('<Return>', lambda e: Bouton.invoke())
Bouton.pack(side=LEFT, padx=5, pady=5)

connect.mainloop()
