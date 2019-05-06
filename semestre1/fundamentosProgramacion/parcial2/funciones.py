#!/usr/bin/python

# Importar librerias
import random
import matplotlib.pyplot as plt
import numpy as np
import math

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


# Punto 1

def first():
    LABEL="Gráfico de la función: √x + ln(x) +2"
    a = []
    
    print(bcolors.HEADER+"\nPunto 1: "+LABEL+bcolors.ENDC)
    #for x in range(-10, 11, 1):
    for x in range(1, 11, 1):
        sol = (math.sqrt(x) + math.log(x) +2)
        a.append(sol)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(a)

    plt.title(LABEL, fontdict=None, loc='center', pad=None)
    plt.grid(True)
    plt.show()


# Punto 2

def second():

    print(bcolors.HEADER+"\nResolver el sistema de ecuaciones de 2*2"+bcolors.ENDC)
    m = """
    ax + by = c
    dx + ey = f
    """
    print(bcolors.OKGREEN+m+bcolors.ENDC)
    print(bcolors.WARNING+"Ingrese los coeficientes de la ecuación separados por espacio: "+bcolors.ENDC)
    a, b, c, d, e, f = input().split()
    a = int(a) 
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    print(bcolors.WARNING+'\nLa ecuación es: '+bcolors.ENDC)
    m = """
    {}x + {}y = {}
    {}x + {}y = {}
    """.format(a,b,c,d,e,f)
    print(bcolors.WARNING+m+bcolors.ENDC)
    continuar = input(bcolors.HEADER+"Es correcto? (Y/N)"+bcolors.ENDC)
    if (continuar == "y" or continuar == "Y"):
        A = np.array([ [a,b], [d,e] ])
        B = np.array([c,f])
        Z = np.linalg.solve(A,B)
        x = Z[0]
        y = Z[1]
        print(bcolors.OKGREEN+'\nLa solución de la ecuación es:'+bcolors.ENDC)
        print(bcolors.OKGREEN+'\nx = {} , y = {}\n'.format(x,y)+bcolors.ENDC)
    elif (continuar == "n" or continuar == "N"):
        print(bcolors.OKGREEN+'\nSaliendo del programa....'+bcolors.ENDC)
        exit()
    else:
        print(bcolors.OKGREEN+'\nDebe digitar Y o N. '+bcolors.ENDC)
        exit()



if __name__ == "__main__":
    print(bcolors.HEADER+"Parcial corte 2\n"+bcolors.ENDC)

    first()
    second()