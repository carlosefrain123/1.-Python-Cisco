""" Ejercicio 2 → Tenemos una lista de equipos de fútbol. Imprime todos los jugadores 
de cada equipo. """
equipos = [
    ["Juan", "Pedro", "Luis"],
    ["Ana", "María", "Sofía"]
]
for i in equipos:
    for j in i:
        print(j)