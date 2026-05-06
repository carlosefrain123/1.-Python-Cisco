""" Ejercicio 5 → Función con tipo incorrecto """
def suma(a,b):
    try:
        suma=a+b
        return suma
    except TypeError:
        return "Error.."
print(suma(10,"2"))