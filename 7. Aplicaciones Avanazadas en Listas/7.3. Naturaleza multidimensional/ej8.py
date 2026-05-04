""" Ejercicio 1 → Cuenta cuántas monedas "M" hay en el mapa
 """
mapa = [
    [".", "M", "."],
    ["M", ".", "M"],
    [".", "M", "."]
]
cont=0
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        """ print(mapa[i][j]) """
        if mapa[i][j]=="M":
            cont+=1
print("Hay ",cont," monedas")