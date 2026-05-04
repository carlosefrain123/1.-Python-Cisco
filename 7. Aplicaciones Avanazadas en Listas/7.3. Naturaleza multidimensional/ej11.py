""" Ejercicio 4 → Imprime solo los números pares del tablero
 """
tablero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(tablero)):
    for j in range(len(tablero[i])):
        if tablero[i][j]%2==0:
            print(tablero[i][j])