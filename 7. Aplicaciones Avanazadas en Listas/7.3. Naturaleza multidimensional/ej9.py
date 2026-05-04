""" Ejercicio 2 → Encuentra la posición del jugador "J"
 """
mapa = [
    [".", ".", "."],
    [".", "J", "."],
    [".", ".", "."]
]
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j]=="J":
            print("Está en la fila ",i, " y en la columna ",j)