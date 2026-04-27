""" Ejercicio 3 → Imprime el nombre y la primera nota de cada estudiante """
notas = [
    [90, 85, 78],   # Ana
    [70, 95, 88],   # Luis
    [60, 75, 92],   # María
]
nombres = ["Ana", "Luis", "María"]

for i in range(len(notas)):
    print(nombres[i],notas[i][0])