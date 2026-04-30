""" Ejercicio 6 → Validar nota
Es válida si está entre 0 y 20
(sistema de notas peruano).
Si no es válida devuelve None.

validar_nota(15)  → 15
validar_nota(-1)  → None
validar_nota(21)  → None """
def validar_nota(nota):
    if nota<0 or nota>20:
        return None
    return nota
print(validar_nota(15))
print(validar_nota(-1))
print(validar_nota(21))
