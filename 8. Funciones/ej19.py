""" Caso 3: Promedio de notas
Usando las funciones anteriores, calcula el promedio
de 3 notas y devuelve su clasificación.
Si alguna nota es inválida devuelve None.

promedio_notas(15, 18, 12) → "Bueno"
promedio_notas(8,  6,  10) → "Desaprobado"
promedio_notas(25, 15, 12) → None """

def validar_nota(nota):
    if nota<0 or nota>20:
        return None
    return nota
def clasificar_nota(nota):
    if validar_nota(nota) is None:
        return "Nota invalida"
    if nota<=10:
        return "Desaprobado"
    elif nota<=13:
        return "Regular"
    elif nota<=15:
        return "Bueno"
    else:
        return "Excelente"
def promedio_notas(n1, n2, n3):
    if validar_nota(n1) is None:
        return None
    if validar_nota(n2) is None:
        return None
    if validar_nota(n3) is None:
        return None
    promedio_notas=(n1+n2+n3)//3
    return clasificar_nota(promedio_notas)
print(promedio_notas(15, 18, 12))
print(promedio_notas(8,  6,  10))
print(promedio_notas(25, 15, 12))