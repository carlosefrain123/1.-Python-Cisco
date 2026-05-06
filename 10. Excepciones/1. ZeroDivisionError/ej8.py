""" Ejercicio 3 → División con input """
try:
    valor=int(input("Ingrese un número: "))
    resultado=100/valor
    print(resultado)
except ZeroDivisionError:
    print("Error")