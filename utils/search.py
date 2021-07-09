import urllib.request
import urllib.response
import urllib.error
from colorama import Fore
from colorama import Style

url = ""
google = ""
duckduckgo = ""
qwant = ""
ecosia = ""


def search():
    global url, google, duckduckgo, qwant, ecosia

    search_words = input("Merci de rentrer le terme que vous rechercher : ")

    try:
        # agent_user = ""
        # headers = {'User-Agent': agent_user}
        # requete = urllib.request.Request(url, None, headers)
        # reponse = urllib.request.urlopen(requete)
        google = "https://www.google.fr/search?hl=fr&q=" + search_words
        duckduckgo = "https://duckduckgo.com/?q=" + search_words
        qwant = "https://www.qwant.com/?l=fr&q=" + search_words
        ecosia = "https://www.ecosia.org/search?q=" + search_words
    except urllib.error.HTTPError as e:
        print("[-] Erreur HTTP :" + str(e.code))
    except urllib.error.URLError as e:
        print("[-] Erreur d'URL : " + e.reason)

    print(Fore. GREEN + "[+] Voici la recherche que vous avez deamndé : \n" + Style.RESET_ALL +
          Fore.YELLOW + "► Google : " + google +
          "\n► DuckDuckGo : " + duckduckgo +
          "\n► Qwant : " + qwant +
          "\n► Ecosia : " + ecosia + Style.RESET_ALL)
