""" Ejercicio 5 → Cuenta cuántas bombas "B" hay en cada fila
 """
campo = [
    ["B", "B", "B", "."],
    [".", ".", "B", "B"],
    ["B", "B", ".", "."]
]
for i in range(len(campo)):
    conteo=0
    for j in range(len(campo[i])):
        """ print(campo[i][j]) """
        if campo[i][j]=="B":
            conteo+=1
    print("En la fila ",i," es: ",conteo)