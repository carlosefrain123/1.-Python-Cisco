""" Tienes una lista de jugadores organizados por equipo.
Tu tarea es:
1. Imprimir todos los jugadores con su equipo
2. Encontrar el equipo con más jugadores
3. Imprimir el primer jugador de cada equipo """
equipos = [
    ["Ana", "Luis", "Pedro", "Rosa"],   # equipo rojo
    ["Jorge", "María"],                  # equipo azul
    ["Carlos", "Lucía", "Diego"]        # equipo verde
]
nombres_equipos = ["Rojo", "Azul", "Verde"]
print("1. Imprimir todos los jugadores con su equipo")
for i in range(len(equipos)):
    for j in range(len(equipos[i])):
        print(equipos[i][j],"-> Equipo",nombres_equipos[i])
print("2. Encontrar el equipo con más jugadores")
max_cont=0
for i in range(len(equipos)):
    cont=0
    for j in range(len(equipos[i])):
        cont+=1
    if cont>max_cont:
        max_cont=cont
        max_equipo=nombres_equipos[i]
print(max_equipo,"->",max_cont)
print("3. Imprimir el primer jugador de cada equipo")
for i in range(len(equipos)):
    print(equipos[i][0])