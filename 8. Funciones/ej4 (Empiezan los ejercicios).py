""" 
caso 1: Es válida si está entre 0 y 120 años.
Si no es válida devuelve None.

validar_edad(25)   → 25
validar_edad(-1)   → None
validar_edad(121)  → None """

def validar_edad(edad):
    if edad<0 or edad>120:
        return None
    return edad