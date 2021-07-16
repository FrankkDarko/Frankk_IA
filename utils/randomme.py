import random
import requests
from bs4 import BeautifulSoup
from colorama import Fore
from colorama import Style
from blagues_api import BlaguesAPI
import asyncio


def faituneblague():
    blagues = BlaguesAPI(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjAwNTQ5NjM1MDY3MDg0ODAwIiwibGltaXQiOjEwMCwia2V5IjoiM1lne"
        "nMxdjNWV1NZSHhkcFR5U1FQSjFFOW9lTHd5aHNtY1JWbzl1dGRKTTU5NEZ2ejgiLCJjcmVhdGVkX2F0IjoiMjAyMS0wNy0xNlQxNTozNDoxNysw"
        "MDowMCIsImlhdCI6MTYyNjQ0OTY1N30.0-ldZbArp0y0cjfi8kpDQhDXE2C6rxB3C5t9DbIvYeY")

    async def blague():
        blg = await blagues.random()
        blg_joke = blg.joke
        blg_answer = blg.answer
        print(
            Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTGREEN_EX + blg_joke + "\n" + Fore.RED + Style.BRIGHT +
            "IA > " + Fore.LIGHTMAGENTA_EX + blg_answer + Style.RESET_ALL)

    asyncio.run(blague())


def randomme():
    print(Style.RESET_ALL + Fore.GREEN + "Bienvenue dans Random Me\n")

    print("Options :\n" +
          Fore.RED + "[1] " + Fore.YELLOW + " chiffre aléatoire entre 0 et 1000\n" +
          Fore.RED + "[2] " + Fore.YELLOW + " chiffre aléatoire entre deux valeurs définit par vous\n" +
          Fore.RED + "[3] " + Fore.YELLOW + " mot aléatoire en français\n" +
          Fore.RED + "[4] " + Fore.YELLOW + " mot aléatoire en anglais\n" +
          Fore.RED + "[5] " + Fore.YELLOW + " blague aléatoire\n")

    choix = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Votre choix : " + Fore.LIGHTCYAN_EX)

    if choix == "1":
        resrange = random.randint(0, 1000)
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Résultat : "
              + Fore.GREEN + Style.BRIGHT + str(resrange) + Style.RESET_ALL)

    if choix == "2":
        min_val = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Valeur minimum : " + Fore.LIGHTCYAN_EX)
        max_val = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Valeur maximum : " + Fore.LIGHTCYAN_EX)
        resrange = random.randint(int(min_val), int(max_val))
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Résultat : "
              + Fore.GREEN + Style.BRIGHT + str(resrange) + Style.RESET_ALL)

    if choix == "3":
        requete = requests.get("https://www.motsqui.com/mots-aleatoires.php?Submit=Nouveau+mot")
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")
        mot = soup.find("b")
        mot_fin = str(mot).replace("<b>", "").replace("</b>", "")
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Résultat : "
              + Fore.GREEN + Style.BRIGHT + mot_fin + Style.RESET_ALL)

    if choix == "4":
        requete = requests.get("https://randomword.com/")
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")
        mot = soup.find("div", {"id": "random_word"})
        mot_fin = str(mot).replace('"', "").replace("</div>", "").replace("<div id=random_word>", "")
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Résultat : "
              + Fore.GREEN + Style.BRIGHT + mot_fin + Style.RESET_ALL)

    if choix == "5":
        faituneblague()

