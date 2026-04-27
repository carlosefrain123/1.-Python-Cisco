""" Ejercicio 3 → Cambia todos los "X" por "O" (liberar asientos ocupados) """
cine = [
    ["O", "X", "O"],
    ["X", "O", "X"],
    ["O", "O", "X"]
]

for i in range(len(cine)):
    for j in range(len(cine[i])):
        if cine[i][j]=="X":
            cine[i][j]="O"
        print(cine[i][j])