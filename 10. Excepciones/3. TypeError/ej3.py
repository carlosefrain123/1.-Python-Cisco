""" Ejercicio 2 → Llamar algo que no es función """
try:
    numero = 5
    numero()
except TypeError:
    print("Error: un número no es una función")