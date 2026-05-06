""" Ejercicio 2 → Método inexistente en lista """
try:
    lista = [1, 2, 3]
    lista.upper()
except AttributeError:
    print("Error: las listas no tienen el método upper()")