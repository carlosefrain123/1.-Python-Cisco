""" Ejercicio 5 → Cuenta cuántos estudiantes tienen más de 80 en la segunda materia """
notas = [
    [90, 85, 78],   # Ana
    [70, 95, 88],   # Luis
    [60, 75, 92],   # María
    [80, 85, 102],   # Efrain
]
cont=0
for i in range(len(notas)):
    if(notas[i][1]>80):
        print(notas[i][1])
        cont+=1
print("Total: ",cont)