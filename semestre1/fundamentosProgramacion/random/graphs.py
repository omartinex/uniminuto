from __future__ import division
#!/usr/bin/python

# Importar librerias
import random
import matplotlib.pyplot as plt
import numpy as np

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

def plotter():
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []

    for x in range(-10000, 10001, 1):
        y = x**2
        a.append(x)
        b.append(y)

    for x in range(-10000, 10001, 1):
        y = x**3
        c.append(x)
        d.append(y)

    for x in range(-100, 101, 1):
        y = x**4
        e.append(x)
        f.append(y)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(a, b)
    axes.plot(c, d)

    # axes.plot(e, f)
    plt.grid(True)
    plt.show()


def plotter2():
    x = np.arange(-100, 101)

    #plt.plot(x, x)
    plt.plot(x, x**2)
    plt.plot(x, x**3)
    plt.plot(x, x**4)
    plt.legend(['y = x^2', 'y = x^3', 'y = x^4'], loc='upper left')
    plt.show()


if __name__ == "__main__":
    print(bcolors.HEADER+"Taller Random"+bcolors.ENDC)
    print("")

    # plotter()
    plotter2()
