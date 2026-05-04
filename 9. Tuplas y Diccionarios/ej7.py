""" Ejercicio 3: Temperatura por ciudad
Un programa que:

Pide nombres de ciudades y sus temperaturas
Guarda todo en un diccionario
Al final muestra las ciudades ordenadas con su temperatura promedio """
diccionario={}
while True:
    nombre_ciudad=input("Ingrese el nombre de la ciudad: ")
    if nombre_ciudad=="":
        break
    temperatura=int(input("Ingrese la temperatura: "))
    if temperatura not in range(0,21):
        break
    if nombre_ciudad in diccionario:
        print("Ya existe")
        diccionario[nombre_ciudad]+=(temperatura,)
    else:
        print("Guardando")
        diccionario[nombre_ciudad]=(temperatura,)
for nombre_ciudad in diccionario:
    total=0
    conteo=0
    for temperatura in diccionario[nombre_ciudad]:
        total+=temperatura
        conteo+=1
    promedio=total/conteo
    print(nombre_ciudad,", su temperatura es: ",promedio)