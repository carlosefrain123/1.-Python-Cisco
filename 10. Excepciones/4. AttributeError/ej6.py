""" Ejercicio 5 → Validar con AttributeError """
def convertir_mayusculas(valor):
    try:
        return valor.upper()
    except AttributeError:
        return "Error: solo los textos tienen upper()"

print(convertir_mayusculas("hola"))  # HOLA
print(convertir_mayusculas(123))     # Error