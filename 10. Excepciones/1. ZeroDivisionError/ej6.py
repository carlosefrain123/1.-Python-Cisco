""" Ejercicio 5 → División con validación """
def promedio(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error..."
print(promedio(10,0))