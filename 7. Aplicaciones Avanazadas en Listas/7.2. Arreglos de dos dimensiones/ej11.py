""" Ejercicio 4 → Encuentra al estudiante con la nota más baja en la segunda materia """
notas = [
    [15, 9, 12],   # Carlos
    [10, 15, 16],   # Ana
    [19, 11, 13],   # Luis
]
nombres = ["Carlos", "Ana", "Luis"]

peor_alumno=nombres[0]
notas_menores=notas[0][1]

for i in range(len(notas)):
    """ print(notas[i][1]) """
    if notas[i][1] < notas_menores:
        notas_menores=notas[i][1]
        peor_alumno=nombres[i]
print(peor_alumno,"->",notas_menores)