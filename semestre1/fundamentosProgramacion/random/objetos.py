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


nombre = ["Tony", "Steve", "Thor", "Oscar", "Juan", "Nico", "William",
          "Andres", "Dave", "Carlos", "Cesar", "Sebas", "Jairo", "Diego"]
apellido = ["Stark", "Rogers", "Odinson", "Maritnez",
            "Russi", "Amado", "Gutierrez", "Cortes", "Rojas", "Umba"]
sueldo = [100, 200, 300, 400, 500, 600,
          700, 800, 900, 1000, 2000, 3000, 4000]


class trabajador:

    def __init__(self, name, apellido, sueldo):
        self.name = name
        self.apellido = apellido
        self.sueldo = sueldo


def create_workers():
    empleados = []
    for i in range(101):
        worker = trabajador(random.choice(nombre), random.choice(
            apellido), random.choice(sueldo))
        empleados.append(worker)
        print("El trabajador {} {} tiene de sueldo: ${}.".format(
            empleados[i].name, empleados[i].apellido, empleados[i].sueldo))

    # print(empleados)


if __name__ == "__main__":
    print(bcolors.HEADER+"Información trabajadores"+bcolors.ENDC)
    print("")
    create_workers()
