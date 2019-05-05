NOTAS = [0, 4, 3, 2]

NOMBRE = ["Hugo", "Jorge", "Haberto", "Larry"]
APELLIDO = ["Norrea", "Nitales", "Camelo", "Caverga"]

for i in range(len(NOMBRE)):
    print(NOMBRE[i], APELLIDO[i], NOTAS[i])
    if (NOTAS[i] < 3):
        print("perdio\n")
    else:
        print("paso\n")
