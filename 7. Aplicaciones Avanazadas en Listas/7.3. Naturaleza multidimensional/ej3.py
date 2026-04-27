""" Ejercicio 1 → Cuenta cuántas bombas "B" hay en el mapa """
mapa = [
    [".", "B", "."],
    ["B", ".", "."],
    [".", ".", "B"]
]
cont=0
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j]=="B":
            cont+=1
print("Hay ",cont," bombas")