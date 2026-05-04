""" Ejercicio 5: Control de inventario
Un programa que:

Pide nombres de productos y sus cantidades
Guarda todo en un diccionario
Al final muestra los productos ordenados con su cantidad promedio """
diccionario={}
while True:
    nombre_producto=input("Ingrese el nombre de los productos: ")
    if nombre_producto=="":
        break
    cantidad=int(input("Ingrese la cantidad de productos: "))
    if cantidad not in range(0,1001):
        break
    if nombre_producto in diccionario:
        print("***Producto ya guardado***")
        diccionario[nombre_producto]+=(cantidad,)
    else:
        print("***Guardando...")
        diccionario[nombre_producto]=(cantidad,)
for nombre_producto in diccionario:
    total=0
    conteo=0
    for cantidad in diccionario[nombre_producto]:
        total+=cantidad
        conteo+=1
    promedio=total/conteo
    print(nombre_producto,"->",promedio)