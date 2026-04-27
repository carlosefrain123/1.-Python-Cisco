""" Ejercicio 2 → Del mismo salón, encuentra quién tiene la nota más alta en la primera materia. """
notas = [
    [90, 85, 78],   # Ana
    [70, 95, 88],   # Luis
    [60, 75, 92],   # María
]
nombres = ["Ana", "Luis", "María"]
num_mayor=notas[0][0]
mejor=nombres[0]
for i in range(len(notas)):
    if notas[0][i]>num_mayor:
        num_mayor=notas[0][i]
print(mejor,num_mayor)