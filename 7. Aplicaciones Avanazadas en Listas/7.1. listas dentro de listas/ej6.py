""" Ejercicio 4 → Imprime todos los elementos de todas las listas """
numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        print(numeros[i][j])