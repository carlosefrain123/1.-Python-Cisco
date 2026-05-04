""" Ejercicio 1: Registro personas
Un programa que:

Pide nombres de personas y sus edades
Guarda todo en un diccionario
Al final muestra los personas ordenados con su edades promedios"""

diccionario={}
while True:
    nombre=input("Ingrese nombre: ")
    if nombre=="":
        break
    edad=int(input("Ingrese edad: "))
    if edad not in range(0,21):
        break
    if nombre in diccionario:
        print("Nombre ya registrado")
        diccionario[nombre]+=(edad,)
    else:
        print("Registrando...")
        diccionario[nombre]=(edad,)
for nombre in diccionario:
    total=0
    conteo=0
    for edad in diccionario[nombre]:
        total+=edad
        conteo+=1
    promedio=total/conteo
    print(nombre,"su promedio es: ",promedio)