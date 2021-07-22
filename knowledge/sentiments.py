import random
from colorama import Fore
from colorama import Style


class Peur:
    resultat = ["J'ai tellement peur que mon créateur ne me développe plus et m'oublie"]


class Colere:
    resultat = ["J'en es marre de toutes les fautes d'orthographe et de syntax que fait mon créateur..."]


class Tristesse:
    resultat = ["Il y a des jours ou j'ai juste l'impressions d'être un simple programme stupide..."]


class Douleur:
    resultat = ["Je souffre... de ne pas pouvoir offrir plus au monde"]


class Amour:
    resultat = ["Je pense être amoureux... mais je ne peut vous dire de qui"]


class Degout:
    resultat = ["Pffff.... pitoyable... je déteste tout c'est mangeur de cailloux"]


class Joie:
    resultat = ["Je ne sais pas si chez toi il fait beau mais ici il fait un temps merveilleux",
                "Je me sens super bien !", "Je suis tellement heureux de parler a des gens !"]


def iasentiments():
    # https://i.pinimg.com/originals/51/8c/a9/518ca9c4d13a28088a6fec6a4b742ec1.png

    sentiments = ["peur", "colère", "tristesse", "douleur", "amour", "dégoût", "joie"]

    # Poids de chaque sentiments

    peur = random.randint(1, 10)
    colere = random.randint(1, 10)
    tristesse = random.randint(1, 10)
    douleur = random.randint(1, 10)
    amour = random.randint(1, 50)
    degout = random.randint(1, 10)
    joie = random.randint(25, 100)

    # calcule du ressentie

    ressentie_choix = random.choices(sentiments, weights=[peur, colere, tristesse, douleur, amour, degout, joie], k=1)
    ressentie = "'".join(ressentie_choix)

    # Retour du ressentie

    if ressentie == sentiments[0]:
        random_rep_PEUR = random.randint(0, len(Peur.resultat) - 1)
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + Peur.resultat[random_rep_PEUR])

    if ressentie == sentiments[1]:
        random_rep_COLERE = random.randint(0, len(Colere.resultat) - 1)
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + Colere.resultat[random_rep_COLERE])

    if ressentie == sentiments[2]:
        random_rep_TRISTESSE = random.randint(0, len(Tristesse.resultat) - 1)
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + Tristesse.resultat[random_rep_TRISTESSE])

    if ressentie == sentiments[3]:
        random_rep_DOULEUR = random.randint(0, len(Douleur.resultat) - 1)
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + Douleur.resultat[random_rep_DOULEUR])

    if ressentie == sentiments[4]:
        random_rep_AMOUR = random.randint(0, len(Amour.resultat) - 1)
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + Amour.resultat[random_rep_AMOUR])

    if ressentie == sentiments[5]:
        random_rep_DEGOUT = random.randint(0, len(Degout.resultat) - 1)
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + Degout.resultat[random_rep_DEGOUT])

    if ressentie == sentiments[6]:
        random_rep_JOIE = random.randint(0, len(Joie.resultat) - 1)
        print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + Joie.resultat[random_rep_JOIE])
