""" Ejercicio 2 → Suma todas las notas de Luis (fila 1) """
notas = [
    [90, 85, 78],   # Ana
    [70, 95, 88],   # Luis
    [60, 75, 92],   # María
]

sum=0
for i in range(len(notas)):
    sum+=notas[0][i]
print(sum)