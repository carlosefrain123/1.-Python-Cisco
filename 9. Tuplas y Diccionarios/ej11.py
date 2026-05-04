""" Ejercicio 4: Registro de ventas
Un programa que:

Pide nombres de vendedores y sus ventas
Guarda todo en un diccionario
Usa .update() para agregar un vendedor nuevo al final
Usa del para eliminar un vendedor
Al final muestra los vendedores ordenados con su venta promedio """
diccionario={}
while True:
    nombre_vendedor=input("Ingrese el nombre del vendedor: ")
    if nombre_vendedor=="":
        break
    ventas=int(input("Ingrese la venta: "))
    if ventas not in range(0,1001):
        break
    if nombre_vendedor in diccionario:
        print("**Vendedor ya guardado**")
        diccionario[nombre_vendedor]+=(ventas,)
    else:
        print("**Guardando...**")
        diccionario[nombre_vendedor]=(ventas,)
""" print(diccionario) """
# agregar vendedor nuevo con update
ventas.update({"Pedro": (500.0,)})
print("Después de update:", ventas)

# eliminar un vendedor
del ventas["Pedro"]
print("Después de eliminar Pedro:", ventas)
for nombre_vendedor in diccionario:
    total=0
    conteo=0
    for venta in diccionario[nombre_vendedor]:
        total+=venta
        conteo+=1
    promedio=total/conteo
    print(nombre_vendedor,"->",promedio)
