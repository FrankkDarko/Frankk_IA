from colorama import Fore
from colorama import Style
import csv
import pandas as pd


def help_me():
    print("Voici les commandes disponible :")

    with open("knowledge/info_help.csv", newline='') as f:
        lire = pd.read_csv(f)
        nom_value = lire["nom"].values
        alias_value = lire["alias"].values
        desc_value = lire["description"].values

        for i in range(len(lire)):
            print("Commande : " + nom_value[i] +
                  "\n             └► " + "Alias : [" + alias_value[i] + "]" + "  ||  Description : " + desc_value[i])
