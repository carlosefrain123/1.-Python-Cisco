""" Ejercicio 1 → Tenemos las notas de 3 estudiantes en 3 materias. Imprime la nota de cada uno. """
notas = [
    [90, 85, 78],   # Ana
    [70, 95, 88],   # Luis
    [60, 75, 92],   # María
]
nombres = ["Ana", "Luis", "María"]

for i in range(len(notas)):
    print(nombres[i],notas[i])