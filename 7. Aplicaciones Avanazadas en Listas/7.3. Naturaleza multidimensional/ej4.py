""" Ejercicio 2 → Encuentra la posición de la estrella "E" """
mapa = [
    [".", ".", "."],
    [".", ".", "E"],
    [".", ".", "."]
]

for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j]=="E":
            print("Posición: Fila: ",i," | Columna: ",j)