""" Tienes una lista de frutas organizadas por temporada.
Tu tarea es:
1. Imprimir todas las frutas de verano (primera lista)
2. Contar cuántas frutas hay en total
3. Imprimir la última fruta de cada temporada """
frutas = [
    ["mango", "sandía", "papaya"],      # verano
    ["naranja", "mandarina", "limón"],  # invierno
    ["fresa", "uva", "manzana"]         # otoño
]
total=0
for i in range(len(frutas)):
    for j in range(len(frutas[i])):
        total+=1
    print(f"***Frutas de verano: {frutas[i][j]}")
for i in range(len(frutas)):
    for j in range(len(frutas[i])):
        total+=1
print(f"**Frutas en total: {total}")
for i in range(len(frutas)):
    for j in range(len(frutas[i])):
        print
    print(f"*últimas frutas: {frutas[i][j]}")