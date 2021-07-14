import string
from colorama import Fore
from colorama import Style


def cryptor():
    print(Style.RESET_ALL + Fore.GREEN + "Bienvenue dans Cryptor\n")

    choix = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Voulez-vous crypter ou décrypter ? "
                  + Fore.LIGHTCYAN_EX).lower()

    if choix == "crypter":
        cryptage = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX +
                         "Crypter en : ROT13, césar, vigenère ? "
                         + Fore.LIGHTCYAN_EX)

        if cryptage == "ROT13":
            phrase = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "entre ta phrase : "
                           + Fore.LIGHTCYAN_EX)
            string_lower = string.ascii_lowercase
            string_upper = string.ascii_uppercase
            letters = string.ascii_letters
            key = 13
            phrase_crypter = ""
            for character in phrase:
                if character in string_lower:
                    phrase_crypter += string_lower[(string_lower.index(character) + key) % len(string_lower)]
                elif character in string_upper:
                    phrase_crypter += string_upper[(string_upper.index(character) + key) % len(string_upper)]
                elif character not in letters:
                    phrase_crypter += character
            print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Message crypter : "
                  + Fore.GREEN + Style.BRIGHT + phrase_crypter + Style.RESET_ALL)

        if cryptage == "césar":
            phrase = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "entre ta phrase : "
                           + Fore.LIGHTCYAN_EX)
            key = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "entre la clé de décalage : "
                        + Fore.LIGHTCYAN_EX)
            letters = string.ascii_letters
            phrase_crypter = ""
            for character in phrase:
                if character not in letters:
                    phrase_crypter += character
                else:
                    phrase_crypter += letters[(letters.index(character) + int(key)) % len(letters)]
            print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Message crypter : "
                  + Fore.GREEN + Style.BRIGHT + phrase_crypter + Style.RESET_ALL)

        if cryptage == "vigenère":
            phrase = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "entre ta phrase : "
                           + Fore.LIGHTCYAN_EX)
            key = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "entre la clé de cryptage ex: aabb : "
                        + Fore.LIGHTCYAN_EX)
            letters = string.ascii_letters
            phrase_crypter = ""
            for index, character in enumerate(phrase):
                key_index = letters.index(key[index % len(key)])
                if character not in letters:
                    phrase_crypter += character
                else:
                    phrase_crypter += letters[(letters.index(character) + key_index) % len(letters)]
            print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Message crypter : "
                  + Fore.GREEN + Style.BRIGHT + phrase_crypter + Style.RESET_ALL)

    if choix == "décrypter":
        decryptage = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX +
                           "Décrypter du : ROT13, césar, vigenère ? "
                           + Fore.LIGHTCYAN_EX)

        if decryptage == "ROT13":
            phrase = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "entre ta phrase : "
                           + Fore.LIGHTCYAN_EX)
            string_lower = string.ascii_lowercase
            string_upper = string.ascii_uppercase
            letters = string.ascii_letters
            key = -13
            phrase_decrypter = ""
            for character in phrase:
                if character in string_lower:
                    phrase_decrypter += string_lower[(string_lower.index(character) + key) % len(string_lower)]
                elif character in string_upper:
                    phrase_decrypter += string_upper[(string_upper.index(character) + key) % len(string_upper)]
                elif character not in letters:
                    phrase_decrypter += character
            print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Message décrypter : "
                  + Fore.GREEN + Style.BRIGHT + phrase_decrypter + Style.RESET_ALL)

        if decryptage == "césar":
            phrase = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "entre ta phrase : "
                           + Fore.LIGHTCYAN_EX)
            key = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "entre la clé de décalage : "
                        + Fore.LIGHTCYAN_EX)
            letters = string.ascii_letters
            phrase_decrypter = ""
            for character in phrase:
                if character not in letters:
                    phrase_decrypter += character
                else:
                    phrase_decrypter += letters[(letters.index(character) - int(key)) % len(letters)]
            print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Message décrypter : "
                  + Fore.GREEN + Style.BRIGHT + phrase_decrypter + Style.RESET_ALL)

        if decryptage == "vigenère":
            phrase = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "entre ta phrase : "
                           + Fore.LIGHTCYAN_EX)
            key = input(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "entre la clé de cryptage ex: aabb : "
                        + Fore.LIGHTCYAN_EX)
            letters = string.ascii_letters
            phrase_decrypter = ""
            for index, character in enumerate(phrase):
                key_index = letters.index(key[index % len(key)])
                if character not in letters:
                    phrase_decrypter += character
                else:
                    phrase_decrypter += letters[(letters.index(character) - key_index) % len(letters)]
            print(Fore.RED + Style.BRIGHT + "IA > " + Fore.LIGHTYELLOW_EX + "Message décrypter : "
                  + Fore.GREEN + Style.BRIGHT + phrase_decrypter + Style.RESET_ALL)
