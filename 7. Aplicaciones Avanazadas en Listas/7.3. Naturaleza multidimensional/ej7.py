""" Ejercicio 5 → Cuenta cuántos jugadores "J" hay en cada fila """
campo = [
    ["J", ".", "J", "J"],
    [".", "J", ".", "."],
    ["J", "J", ".", "J"]
]

for i in range(len(campo)):
    contador=0
    for j in range(len(campo[i])):
        if campo[i][j]=="J":
            contador+=1
    print("Tercera Prueba: Fila ",i," hay ",contador)