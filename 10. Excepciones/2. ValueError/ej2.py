""" Ejercicio 1 → Convertir texto a número """
try:
    int("Hola")
except ValueError:
    print("Error: Eso no es un número")