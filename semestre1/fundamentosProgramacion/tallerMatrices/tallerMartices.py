#!/usr/bin/python

# Importar librerias
import numpy as np
import sys

# Imprimir la matrix completa
np.set_printoptions(threshold=sys.maxsize)

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

# Vector con los numeros de 1 a 9


def vector():
    print(bcolors.HEADER+"Vector con los numeros de 1 a 9"+bcolors.ENDC)
    vector = []
    for x in (range(1, 10)):
        vector.append(x)
    print(bcolors.OKGREEN)
    print(vector)
    print(bcolors.ENDC)


# Vector con los numeros de la serie 2*n+3 desde n=4 hasta n=100
def serie():
    print(bcolors.HEADER +
          "Vector con los numeros de la serie 2*n+3 desde n=4 hasta n=100"+bcolors.ENDC)
    serie = []
    for n in (range(4, 101)):
        serie.append(2*n+3)
    print(bcolors.OKGREEN)
    print(serie)
    print(bcolors.ENDC)

# Matriz de 3*3 con los numeros del 1 al 9


def matrix3x3():
    print(bcolors.HEADER+"Matriz de 3*3 con los numeros del 1 al 9"+bcolors.ENDC)
    matrix3x3 = np.arange(1, 10).reshape(3, 3)
    print(bcolors.OKGREEN)
    print(matrix3x3)
    print(bcolors.ENDC)


# Matriz de 30*50 con el producto de la posicion de la fila por la posicion de la columna


def matrix30x50():
    matrix30x50 = np.arange(1, 1501).reshape(30, 50)
    # matrix10x10 = np.arange(1, 101).reshape(10, 10)
    # print(matrix30x50)
    print(bcolors.HEADER+"Matriz de 30*50 con el producto de la posicion de la fila por la posicion de la columna"+bcolors.ENDC)
    # print("A[0][0] =", matrix10x10[0][0])
    for i in range(10):
        for j in range(10):
            matrix30x50[i][j] = (i+1)*(j+1)

    print(bcolors.OKGREEN)
    print(matrix30x50)
    print(bcolors.ENDC)


if __name__ == "__main__":
    print(bcolors.HEADER+"Taller Matrices y Vectores"+bcolors.ENDC)
    print("")
    vector()
    serie()
    matrix3x3()
    matrix30x50()
