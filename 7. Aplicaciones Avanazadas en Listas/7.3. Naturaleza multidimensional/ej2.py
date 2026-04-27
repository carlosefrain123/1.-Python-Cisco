""" Ejercicio 2 → Tenemos un estacionamiento. Cuenta cuántos espacios libres "L" hay en total. """
estacionamiento = [
    ["L", "O", "L"],
    ["O", "L", "O"],
    ["L", "L", "O"]
]
cont=0
for i in range(len(estacionamiento)):
    for j in range(len(estacionamiento[i])):
        if (estacionamiento[i][j]=="L"):
            cont+=1
print(cont)