""" Imaginemos el siguiente problema:

necesitas un programa para calcular los promedios de tus alumnos;
el programa pide el nombre del alumno seguido de su calificación;
los nombres son ingresados en cualquier orden;
el ingresar un nombre vacío finaliza el ingreso de los datos 
(Nota 1: ingresar una puntuación vacía generará la excepción ValueError, 
pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de 
excepciones en el segundo parte de la serie del curso Fundamentos de Python)
una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.

output:
    Ingresa el nombre del estudiante: Bob
Ingresa la calificación del estudiante (0-10): 7
Ingresa el nombre del estudiante: Andy
Ingresa la calificación del estudiante (0-10): 3
Ingresa el nombre del estudiante: Bob
Ingresa la calificación del estudiante (0-10): 2
Ingresa el nombre del estudiante: Andy
Ingresa la calificación del estudiante (0-10): 10
Ingresa el nombre del estudiante: Andy
Ingresa la calificación del estudiante (0-10): 3
Ingresa el nombre del estudiante: Bob
Ingresa la calificación del estudiante (0-10): 9
Ingresa el nombre del estudiante:
Andy : 5.333333333333333
Bob : 6.0 """

diccionario={}
while True:
    nombre_estudiante=input("Ingrese el nombre del estudiante")
    if nombre_estudiante=="":
        break
    nota_estudiante=int(input("Ingrese la nota del estudiante: "))
    if nota_estudiante not in range(0,11):
        break
    if nombre_estudiante in diccionario:
        diccionario[nombre_estudiante]+=(nota_estudiante,)
    else:
        diccionario[nombre_estudiante]=(nota_estudiante,)
for nombre_estudiante in sorted(diccionario.keys()):
    agregar_nota=0
    conteo=0
    for nota_estudiante in diccionario[nombre_estudiante]:
        agregar_nota+=nota_estudiante
        conteo+=1
    print(nombre_estudiante,":",agregar_nota/conteo)
        