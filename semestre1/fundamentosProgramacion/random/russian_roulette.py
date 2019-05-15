# -*- coding: utf-8 -*-
#!/usr/bin/python

# Importar librerias
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def revolver():
    barril = ["BANG! A tomar tinto en los Olivos (✖╭╮✖) ", "Vive otro día", "Se salvó parce",
              "Se disparó en el pie gueva", "Sigue intentando", "Relaje el pony"]
    random.shuffle(barril)
    for i in barril:
        # print(random.choice(barril))
        if (i == "BANG! A tomar tinto en los Olivos (✖╭╮✖) "):
            print(bcolors.FAIL+"[-] "+i+bcolors.ENDC)
            exit()
        print(bcolors.OKGREEN+"[+] "+i+bcolors.ENDC)
        input("Press Enter to continue...\n")


if __name__ == "__main__":
    print(bcolors.HEADER+"Russian Roulette"+bcolors.ENDC)
    print("")
    revolver()
