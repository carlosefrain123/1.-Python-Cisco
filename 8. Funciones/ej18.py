""" Caso 2: Clasificar nota
Usando la función anterior, clasifica la nota:
0-10  → "Desaprobado"
11-13 → "Regular"
14-16 → "Bueno"
17-20 → "Excelente"
None  → "Nota inválida"

clasificar_nota(8)   → "Desaprobado"
clasificar_nota(12)  → "Regular"
clasificar_nota(15)  → "Bueno"
clasificar_nota(19)  → "Excelente"
clasificar_nota(25)  → "Nota inválida" """
def validar_nota(nota):
    if nota<10 or nota>20:
        return None
    return nota
def clasificar_nota(nota):
    if validar_nota(nota) is None:
        return "Nota Invalida"
    if nota<=10:
        return "Desaprobado"
    elif nota<=13:
        return "Regular"
    elif nota<=15:
        return "Bueno"
    else:
        return "Excelente"
print(clasificar_nota(8))
print(clasificar_nota(12))
print(clasificar_nota(15))
print(clasificar_nota(19))
print(clasificar_nota(25))

