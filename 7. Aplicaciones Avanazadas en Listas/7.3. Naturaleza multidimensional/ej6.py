""" Ejercicio 4 → Imprime solo la diagonal del tablero (donde i == j) """
tablero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(tablero)):
    for j in range(len(tablero[i])):
        if i==j:
            print(tablero[i][j])