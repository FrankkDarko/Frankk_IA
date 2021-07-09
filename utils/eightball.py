import random
from colorama import Fore
from colorama import Style


def oracle():
    print("" + Fore.MAGENTA + Style.BRIGHT +
          "                      _ \n"
          "                     | | \n"
          "  ___  _ __ __ _  ___| | ___ \n"
          " / _ \| '__/ _` |/ __| |/ _ \ \n"
          "| (_) | | | (_| | (__| |  __/ \n"
          " \___/|_|  \__,_|\___|_|\___| \n"
          "\n" + Style.RESET_ALL)
    ask = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Pose ta questions : " + Style.RESET_ALL)
    reponse = random.choice(["oui", "non", "oups je n'en sais rien", "Franchement c'est pas mon problème",
                             "Je pense que au font de toi tu le sais", "Je ne peut pas te dire ce que tu sais",
                             "si tu ne le fait pas tu ne le sera jamais",
                             "demande au tour de toi et fait ce que tu pense être le bon choix",
                             "Probablement", "surment pas", "continue de rêver", "essaie encore", "Bonne chance"
                             ])
    print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------\n"
          + Style.RESET_ALL + Fore.GREEN +
          "    Votre question : " + Style.RESET_ALL + ask + "\n" + Fore.YELLOW + "    Réponse de l'oracle : "
          + Style.RESET_ALL + reponse + Fore.RED + Style.BRIGHT +
          "\n----------------------------------------------------------------------\n" + Style.RESET_ALL)
