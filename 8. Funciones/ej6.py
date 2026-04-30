""" Ejercicio 3 → Días vividos
Usando las funciones anteriores, calcula cuántos días
ha vivido una persona desde su nacimiento hasta hoy.
Si la edad es inválida devuelve None.

dias_vividos(1)  → 365
dias_vividos(2)  → 730
dias_vividos(-1) → None """

def validar_edad(edad):
    if edad<0 or edad>120:
        return None
    return edad
def dias_vividos(edad):
    if validar_edad(edad) is None:
        return None
    return edad*365
print(dias_vividos(1))
print(dias_vividos(2))
