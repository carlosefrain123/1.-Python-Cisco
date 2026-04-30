""" Usando la función anterior, clasifica la edad:
Recuerda:
Es válida si está entre 0 y 120 años.
Si no es válida devuelve None.
0-12   → "Niño"
13-17  → "Adolescente"
18-64  → "Adulto"
65-120 → "Adulto mayor"
None   → "Edad inválida"

categoria(10)  → "Niño"
categoria(15)  → "Adolescente"
categoria(30)  → "Adulto"
categoria(70)  → "Adulto mayor"
categoria(150) → "Edad inválida" """

def validar_edad(edad):
    if edad<0 or edad>120:
        return None
    return edad
def categoria(edad):
    if categoria(edad) is None:
        return None
    if edad<=10:
        return "Niño"
    elif edad<=15:
        return "Adolescente"
    elif edad<=30:
        return "Adulto"
    else:
        return "Adulto Mayor"
    