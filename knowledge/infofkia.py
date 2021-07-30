from colorama import Fore
from colorama import Style
import os
import time
from datetime import datetime

os.environ['TZ'] = 'Europe/Paris'
time.tzset()

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def ageIA():
    actuel = datetime.now()

    naissance = datetime(2021, 7, 3, 10, 10, 10)

    y = actuel.year - naissance.year
    m = actuel.month - naissance.month
    d = actuel.day - naissance.day

    h = actuel.hour - naissance.hour
    mn = actuel.minute - naissance.minute
    s = actuel.second - naissance.second

    print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Je suis né le 03/07/2021 j'ai donc " + str(y) +
          " ans, " + str(m) + " mois, " + str(d) + " jours, " + str(h) + " heures, " + str(mn) + " minutes, " + str(s)
          + " secondes")
    age = "Je suis né le 03/07/2021 j'ai donc " + str(y) + " ans, " + str(m) + " mois, " + str(d) + " jours, " + str(h) + " heures, " + str(mn) + " minutes, " + str(s) + " secondes"
    return age


def info_of_fkia():
    version_fkia = "FKIA_v_0.0.1.7"  # Versions de Frankk IA

    print(Fore.RED + Style.BRIGHT +
          "---------------------------------------\n"
          "-------------- Frankk IA --------------\n"
          "---------------------------------------\n"
          + Style.RESET_ALL + Fore.LIGHTGREEN_EX +
          "\n"
          "► Version : " + version_fkia +
          "\n"
          "\n"
          "► Développeur : Frankk Darko\n"
          "\n"
          "► Date de création : 2021-07-03\n" +
          "\n"
          "► Github : https://github.com/FrankkDarko\n"
          "\n"
          "► Site : en cours de développement\n"
          "\n"
          "► Contact : frankkdarko@protonmail.com\n"

          + Style.RESET_ALL)
