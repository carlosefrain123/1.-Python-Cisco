""" Ejercicio 4 → Método de texto en lista """
try:
    lista = [1, 2, 3]
    lista.split(",")
except AttributeError:
    print("Error: las listas no tienen el método split()")
