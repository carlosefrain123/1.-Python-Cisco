""" Ejercicio 1 → Método inexistente en número """
try:
    numero = 5
    numero.upper()
except AttributeError:
    print("Error: los números no tienen el método upper()")