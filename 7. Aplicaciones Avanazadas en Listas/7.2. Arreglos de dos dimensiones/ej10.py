""" Ejercicio 3 → Imprime el nombre y primera nota de cada estudiante """
notas = [
    [15, 18, 12],   # Carlos
    [10, 14, 16],   # Ana
    [19, 11, 13],   # Luis
]
nombres = ["Carlos", "Ana", "Luis"]
for i in range(len(notas)):
    print(nombres[i],"->",notas[i][0])