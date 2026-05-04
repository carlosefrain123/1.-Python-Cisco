""" Ejercicio 3 → Cambia todos los "X" por "."
 """
tablero = [
    ["X", ".", "X"],
    [".", "X", "."],
    ["X", ".", "X"]
]
for i in range(len(tablero)):
    for j in range(len(tablero[i])):
        if tablero[i][j]=="X":
            tablero[i][j]="."
        print(tablero[i][j])