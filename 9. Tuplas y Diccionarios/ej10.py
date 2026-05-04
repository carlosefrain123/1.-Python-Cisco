""" Ejercicio 3: Registro de horas trabajadas
Un programa que:

Pide nombres de empleados y sus horas trabajadas
Guarda todo en un diccionario
Al final muestra los empleados ordenados con su promedio de horas """
diccionario={}
while True:
    nombre_empleado=input("Ingrese el nombre del empleado: ")
    if nombre_empleado=="":
        break
    horas_trabajadas=int(input("Ingrese las horas trabajadas: "))
    if horas_trabajadas not in range(0,25):
        break
    if nombre_empleado in diccionario:
        print("Empleado ya registrado")
        diccionario[nombre_empleado]+=(horas_trabajadas,)
    else:
        print("**Guardando**")
        diccionario[nombre_empleado]=(horas_trabajadas,)
for nombre_empleado in diccionario:
    total=0
    conteo=0
    for horas_trabajadas in diccionario[nombre_empleado]:
        total+=horas_trabajadas
        conteo+=1
    promedio=total/conteo
    """ print(nombre_empleado,"->",total) """
    print(nombre_empleado,"->",promedio)
    """ print(diccionario) """