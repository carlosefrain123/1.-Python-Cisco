""" Ejercicio 2 → División con input """
numeros = [10, 20, 0, 30]
for i in numeros:
    try:
        division=100/i
        print("La división es: ",division)
    except ZeroDivisionError:
        print("La división de",i," es 0")
    