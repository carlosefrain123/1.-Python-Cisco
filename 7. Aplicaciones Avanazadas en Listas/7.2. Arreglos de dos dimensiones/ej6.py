""" Ejercicio 4 → Encuentra al estudiante con la nota más baja en la tercera materia """
notas = [
    [90, 85, 78],   # Ana
    [70, 95, 88],   # Luis
    [60, 75, 92],   # María
]
nombres = ["Ana", "Luis", "María"]

nota_baja=notas[0][2]
peor=nombres[0]
for i in range(len(notas)):
    if notas[i][2]<nota_baja:
        nota_baja=notas[i][2]
        peor=nombres[i]
print(peor,nota_baja)