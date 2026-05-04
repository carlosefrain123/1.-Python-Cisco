""" Ejercicio 2 → Suma todas las notas de Ana (fila 1)
 """
notas = [
    [15, 18, 12],   # Carlos
    [10, 14, 16],   # Ana
    [19, 11, 13],   # Luis
]
nombres = ["Carlos", "Ana", "Luis"]

total=0

for i in range(len(notas)):
    """ print(notas[1][i]) """
    total+=notas[1][i]
print(total)