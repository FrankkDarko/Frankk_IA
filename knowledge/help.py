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
            print(Style.RESET_ALL + Fore.GREEN + "Commande : " + Fore.RED + nom_value[i] + Fore.GREEN +
                  "\n             └► " + "Alias : " + Fore.RED + "[" + alias_value[i] + "]"
                  + Fore.GREEN + "  ||  Description : " + Fore.YELLOW + desc_value[i] + Style.RESET_ALL)
