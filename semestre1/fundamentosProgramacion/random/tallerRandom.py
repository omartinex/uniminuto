#!/usr/bin/python

# Importar librerias
import random
import matplotlib.pyplot as plt 
from numpy import mean

# Clase para colorear la terminal


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Vector con numeros aleatorios

def vector():
    print(bcolors.HEADER+"Vector con numeros aleatorios"+bcolors.ENDC)
    global vect 
    vect = []
    for x in (range(0, 10)):
        vect.append(random.randint(1,5))
    print(bcolors.OKGREEN)
    print(vect)
    print(bcolors.ENDC)
    return vect

# Plot function

def plotter():
    media = mean(vect)
    print("La media de los numeros es: {}".format(media))
    plt.axhline(y=media, color='r', linestyle='-')
    #plt.plot()
    plt.plot(vect)
    plt.ylabel('random numbers')
    plt.show()
    


    

if __name__ == "__main__":
    print(bcolors.HEADER+"Taller Random"+bcolors.ENDC)
    print("")
    vector()
    plotter()
   