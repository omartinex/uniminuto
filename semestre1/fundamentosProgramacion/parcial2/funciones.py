from __future__ import division
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


# Plot function

def first():
    a = []
    b = []

    for x in range(-10, 11, 1):
        y = math.sqrt(x)
        a.append(x)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(a, b)

    # axes.plot(e, f)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    print(bcolors.HEADER+"Taller Random"+bcolors.ENDC)
    print("")

    # plotter()
    first()
