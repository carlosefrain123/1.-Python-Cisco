""" Ejercicio 2 → División con input """
try:
    numero=int(input("Ingrese número: "))
    division=100/numero
    print(division)
except ZeroDivisionError:
    print("No se puede dividir entre 0")