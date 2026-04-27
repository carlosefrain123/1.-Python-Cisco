""" Ejercicio 1 → Tenemos un mapa de un juego. Encuentra todas las posiciones donde hay un tesoro "T". """
mapa = [
    [".", ".", "T"],
    [".", "T", "."],
    [".", ".", "."]
]
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j]=="T":
            print("Fila: ",i," | Columna: ",j)