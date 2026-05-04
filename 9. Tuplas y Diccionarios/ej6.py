""" Ejercicio 2: Registro de jugadores
Un programa que:

Pide nombres de jugadores y sus puntos
Guarda todo en un diccionario
Al final muestra los jugadores ordenados con su puntaje promedio """
diccionario={}
while True:
    nombre_jugadores=input("Ingrese el nombre del jugador: ")
    if nombre_jugadores=="":
        break
    puntos=int(input("Ingrese los puntos: "))
    if puntos not in range(0,21):
        break
    if nombre_jugadores in diccionario:
        print("Ya existe")
        diccionario[nombre_jugadores]+=(puntos,)
    else:
        print("Guardando...")
        diccionario[nombre_jugadores]=(puntos,)
""" print(diccionario) """
for nombre_jugadores in diccionario:
    total=0
    conteo=0
    for puntos in diccionario[nombre_jugadores]:
        total+=puntos
        conteo+=1
    promedio=total/conteo
    print(nombre_jugadores,"->",promedio)