""" Ejercicio 1 → División básica
 """
try:
    resultado=10/0
    print(resultado)
except ZeroDivisionError:
    print("Error")