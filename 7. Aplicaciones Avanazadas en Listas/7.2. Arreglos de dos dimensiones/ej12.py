""" Ejercicio 5 → Cuenta cuántos estudiantes tienen más de 15 en la tercera materia """
notas = [
    [15, 18, 12],   # Carlos
    [10, 14, 14],   # Ana
    [19, 11, 17],   # Luis
]
cont=0
for i in range(len(notas)):
    if notas[i][2]>15:
        cont+=1
print("Hay ",cont," alumnos mayores que 15")
        