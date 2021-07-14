from colorama import Fore
from colorama import Style


def info_of_fkia():
    version_fkia = "FKIA_v_0.0.1.5"  # Versions de Frankk IA

    print(Fore.RED + Style.BRIGHT +
          "---------------------------------------\n"
          "-------------- Frankk IA --------------\n"
          "---------------------------------------\n"
          + Style.RESET_ALL + Fore.LIGHTGREEN_EX +
          "\n"
          "► Version : " + version_fkia + "\n"
          "\n"
          "► Développeur : Frankk Darko\n"
          "\n"
          "► Github : https://github.com/FrankkDarko\n"
          "\n"
          "► Site : en cours de développement\n"
          "\n"
          "► Contact : frankkdarko@protonmail.com\n"
          + Style.RESET_ALL)
