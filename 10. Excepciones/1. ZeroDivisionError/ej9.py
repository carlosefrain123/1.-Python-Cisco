""" Ejercicio 4 → División en lista """
numeros = [2, 4, 0, 5]
for i in numeros:
    try:
        division=100/i
        print("-La división es: ",division)
    except ZeroDivisionError:
        print("Error")