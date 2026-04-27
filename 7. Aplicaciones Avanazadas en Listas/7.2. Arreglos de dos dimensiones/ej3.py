""" Ejercicio 1 → Imprime la nota más alta de Ana (fila 0) """
notas = [
    [90, 85, 78],   # Ana
    [70, 95, 88],   # Luis
    [60, 75, 92],   # María
]
nota_mayor=notas[0][0]

for i in range(len(notas)):
    if notas[0][i]>nota_mayor:
        nota_mayor=notas[0][i]
print(nota_mayor)