""" Ejercicio 1 → Imprime la nota más alta de Carlos (fila 0)
 """
notas = [
    [15, 18, 12],   # Carlos
    [10, 14, 16],   # Ana
    [19, 11, 13],   # Luis
]
nombres = ["Carlos", "Ana", "Luis"]
mayor_nota=notas[0][0]

for i in range(len(notas)):
    if notas[0][i]>mayor_nota:
        mayor_nota=notas[0][i]
print(mayor_nota)